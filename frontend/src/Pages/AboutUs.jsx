import backgroundImage from '../Images/AboutUsBG.png';
import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';

export const background = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
};

export const StyledBox = styled(Box)(({ theme }) => ({
  marginTop: -10,
  padding: 25,
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  borderRadius: '8px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.2)',
  backgroundColor: 'rgba(255, 255, 255, 0.8)',
  justifyContent: 'center',
}));

const AboutUs = () => {
  return (
    <div style={background}>
      <StyledBox>
        <Typography variant="h4" sx={{ m: 1, }}>
          About Us
        </Typography>
        <Typography variant="h5" sx={{ m: 1, fontWeight: 'bold' }}>
          Welcome to our company!
        </Typography>
        <Typography variant="h6" sx={{ m: 1, }}>
          We are a team of passionate individuals dedicated to providing exceptional products and services to our customers.
          Our mission is to make a positive impact on student's lives through innovative solutions and outstanding math problems
          and international Olympiad experiences.
        </Typography>
        <Typography variant="h5" sx={{ m: 1, fontWeight: 'bold' }}>
          Our Story
        </Typography>
        <Typography variant="h6" sx={{ m: 1, }}>
          Our journey began in 2022 when a group of like-minded individuals came together with a shared vision.
          We wanted to create something meaningful, something that would make a difference in the world, something
          which will make students love math.
          Over the years, we have grown and evolved, constantly striving for excellence in everything we do.
          Our team of talented professionals works tirelessly to push the boundaries of innovation and deliver
          exceptional results. Students of out site have won numerous gold, silver and bronze medals at the
          international Math Olympiads.
        </Typography>
        <Typography variant="h5" sx={{ m: 1, fontWeight: 'bold' }}>
          Our Values
        </Typography>
        <List>
          <ListItem>
            <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
              Customer Focus:
            </Typography>
            <Typography variant="h6" sx={{ m: 1, }}>
              We prioritize our customers and their needs above everything else.
            </Typography>
          </ListItem>
          <ListItem>
            <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
              Innovation:
            </Typography>
            <Typography variant="h6" sx={{ m: 1, }}>
              We constantly seek new ideas and technologies to develop new learning methods.
            </Typography>
          </ListItem>
          <ListItem>
            <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
              Integrity:
            </Typography>
            <Typography variant="h6" sx={{ m: 1, }}>
              We uphold the highest ethical standards in all our interactions.
            </Typography>
          </ListItem>
          <ListItem>
            <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
              Collaboration:
            </Typography>
            <Typography variant="h6" sx={{ m: 1, }}>
              We believe in the power of teamwork, that's why most of our classes have multiple students.
            </Typography>
          </ListItem>
          <ListItem>
            <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
              Excellence:
            </Typography>
            <Typography variant="h6" sx={{ m: 1, }}>
              Only the math Olympiad tutors are on our site, which makes us the best platform for learning new skills.
            </Typography>
          </ListItem>
        </List>
        <Typography variant="h5" sx={{ m: 1, fontWeight: 'bold' }}>
          Our Team
        </Typography>
        <Typography variant="h6" sx={{ m: 1, }}>
          Behind our success is a diverse and talented team of professionals past Olympians who are passionate about
          what they do. Each member brings a unique set of skills and experiences, contributing to our collective
          success.
          We believe in fostering a culture of continuous learning and growth, empowering our team members to reach
          their full potential.
        </Typography>
        <Typography variant="h5" sx={{ m: 1, fontWeight: 'bold' }}>
          Contact Us
        </Typography>
        <Typography variant="h6" sx={{ m: 1, }}>
          If you have any questions or would like to get in touch, please don't hesitate to reach out to us.
          We would love to hear from you!
        </Typography>
        <Typography variant="h6" sx={{ m: 1, }}>
          Email: tutorsite727@gmail.com
        </Typography>
        <Typography variant="h6" sx={{ m: 1, }}>
          Phone: +995 555 99 00 99
        </Typography>
      </StyledBox>
    </div>
  );
}

export default AboutUs;