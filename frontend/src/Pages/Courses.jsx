import { useState, useEffect } from 'react';
import { styled } from '@mui/system';
import { Container, Grid, Card, CardContent, Button } from '@mui/material';
import { theme } from "../Components/Theme"
import { ThemeProvider } from '@mui/material/styles';
import backgroundImage from '../Images/CoursesBG.png';
import CategoryIcon from '@mui/icons-material/Category';
import PersonIcon from '@mui/icons-material/Person';
import LocalOfferIcon from '@mui/icons-material/LocalOffer';
import { CourseStyledTypography } from "../Components/Styles"
import { HeaderStyledTypography } from "../Components/Styles"
import { Link } from "react-router-dom"

const StyledCard = styled(Card)(({ theme }) => ({
  backgroundColor: '#fffede',
}));

const containerStyle = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
};

export default function Courses() {
  const email = JSON.parse(sessionStorage.getItem("email"))
  const isStudent = JSON.parse(sessionStorage.getItem("isStudent"))
  const [courses, setCourses] = useState([])

  useEffect(() => {
    const handleGetCourses = async () => {
      try {
        const response = await fetch('http://localhost:8000/courses', {
          method: 'GET',
          headers: {
          'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        console.log(data)
        setCourses(data)
      } catch (error) {
        console.error(error);
      }
    };

    handleGetCourses();
  }, []);

  const handleBuyLesson = async (course) => {
    try {
      const data = {
        "subject": course.subject,
        "tutor_mail": course.tutor_mail,
        "lesson_price": course.price,
      }

      let response = await fetch('http://localhost:8000/student/buy_lesson/' + email, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      response = await response.json();
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div style={containerStyle}>
      <ThemeProvider theme={theme}>
        <HeaderStyledTypography variant="h4" align="center">
          Courses
        </HeaderStyledTypography>
        <Container maxWidth="md">
          <Grid container spacing={4}>
            {courses.map((course, index) =>
              <Grid item key={index} xs={12} sm={6} md={4}>
                <StyledCard>
                  <CardContent>
                    <CourseStyledTypography variant="h7">
                      <CategoryIcon />
                      {course.subject}
                    </CourseStyledTypography>
                    <CourseStyledTypography variant="h7">
                      <PersonIcon />
                      <Link to={"/tutors/tutor/" + course.tutor_mail}>
                        {course.tutor_mail}
                      </Link>
                    </CourseStyledTypography>
                    <CourseStyledTypography variant="h7">
                      <LocalOfferIcon />
                      <span>${course.price}</span>
                    </CourseStyledTypography>
                  </CardContent>
                  <Button
                    fullWidth
                    onClick={(e) => handleBuyLesson(course)}
                    disabled={!isStudent}
                    sx ={{ borderRadius: 0, }}>
                    Enroll Now
                  </Button>
                </StyledCard>
              </Grid>
            )}
          </Grid>
        </Container>
      </ThemeProvider>
    </div>
  );
}
