import { useState, useEffect } from 'react';
import backgroundImage from '../Images/TutorsBG.png';
import { HeaderStyledTypography } from "../Components/Styles"
import { Container, Grid, Card, CardContent } from '@mui/material';
import { styled } from '@mui/system';
import Link from '@mui/material/Link';
import { TutorStyledTypography } from "../Components/Styles"

const containerStyle = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
};

const StyledCard = styled(Card)(({ theme }) => ({
  backgroundColor: '#d7faf8',
}));

export default function Tutors() {
  const [tutors, setTutors] = useState([])

  useEffect(() => {
    const handleGetTutors = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutors', {
          method: 'GET',
          headers: {
          'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        console.log(data)
        setTutors(data)
      } catch (error) {
        console.error(error);
      }
    };

    handleGetTutors();
  }, []);

  return (
    <div style={containerStyle}>
      <HeaderStyledTypography variant="h4" align="center">
        Tutors
      </HeaderStyledTypography>
      <Container maxWidth="md">
        <Grid container spacing={4}>
          {tutors.map((tutor, index) =>
            <Grid item key={index} xs={12} sm={6} md={4}>
              <StyledCard>
                <CardContent>
                  <TutorStyledTypography variant="h7">
                    First Name: {tutor.first_name}
                  </TutorStyledTypography>
                  <TutorStyledTypography variant="h7">
                    Last Name: {tutor.last_name}
                  </TutorStyledTypography>
                  <TutorStyledTypography variant="h7">
                    Mail: <Link underline="none" href={`tutors/tutor/${tutor.email}`}>{tutor.email}</Link>
                  </TutorStyledTypography>
                  <TutorStyledTypography variant="h7">
                    Biography:
                      {
                      tutor.biography === ''
                      ? "No info."
                      : tutor.biography
                      }
                  </TutorStyledTypography>
                </CardContent>
              </StyledCard>
            </Grid>
          )}
        </Grid>
      </Container>
    </div>
  );
}


