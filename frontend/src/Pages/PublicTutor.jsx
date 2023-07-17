import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import './Styles.css'
import backgroundImage from '../Images/TutorPublicProfileBG.png';
import { theme } from "../Components/Theme"
import { ThemeProvider } from '@mui/material/styles';
import { HeaderStyledTypography } from "../Components/Styles"
import Box from '@mui/material/Box';
import { styled } from '@mui/system';
import Avatar from '@mui/material/Avatar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const containerStyle = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
};

export const InfoBox = styled(Box)(({ theme }) => ({
  margin: 15,
  borderRadius: '10px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.4)',
  backgroundColor: 'rgba(255, 255, 255, 0.8)',
}));

export const ProfileBox = styled(Box)(({ theme }) => ({
  alignItems: 'center',
  backgroundColor: 'rgba(248, 224, 255, 0)',
  borderRadius: '14px',
  display: 'flex',
  justifyContent: 'center',
  width: "100%",
}));

export const ProfileImage = styled(Box)(({ theme }) => ({
  margin: 15,
  width: 200,
  height: 200,
  display: 'flex',
  alignItems: 'center',
  borderRadius: '200px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.4)',
  backgroundColor: 'rgba(255, 255, 255, 0.3)',
  justifyContent: 'center',
}));

export const ListBox = styled(Box)(({ theme }) => ({
  alignItems: 'center',
  backgroundColor: 'rgba(255, 255, 255, 0)',
  borderRadius: '14px',
  display: 'flex',
  flexDirection: 'row',
  height: 400,
  justifyContent: 'center',
  margin: 'auto',
  marginTop: 20,
  width: "90%",
  padding: 25,
}));

export const ListItemBox = styled(Box)(({ theme }) => ({
  marginLeft: 20,
  marginRight: 30,
  width: '100%',
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  borderRadius: '10px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.4)',
  backgroundColor: 'rgba(255, 255, 255, 0.5)',
  justifyContent: 'center',
}));

const PublicTutor = () => {
  const { email } = useParams();
  const visitor_mail = JSON.parse(sessionStorage.getItem('email'));

  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [biography, setBiography] = useState('');
  const [profileAddress, setProfileAddress] = useState('');

  const [courses, setCourses] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [reviewText, setReviewText] = useState('');
  const [is_tutor_student, setIsTutorStudent] = useState(false);
  const [rating, setRating] = useState(0); // New state for star rating

  const [messageToTutor, setMessageToTutor] = useState('');

  useEffect(() => {
    const handleGetTutor = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const tutorData = await response.json();
        setFirstName(tutorData['first_name']);
        setLastName(tutorData['last_name']);
        setBiography(tutorData['biography']);
        setProfileAddress(tutorData['profile_address']);
        setIsTutorStudent(tutorData['is_tutor_student']); // Retrieve the is_tutor_student flag
      } catch (error) {
        console.error(error);
      }
    };
    handleGetTutor();
  }, []);

  useEffect(() => {
    const handleGetCourses = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/courses/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const coursesData = await response.json();
        setCourses(coursesData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetCourses();
  }, []);

  useEffect(() => {
    const handleGetReviews = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/reviews/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const reviewsData = await response.json();
        setReviews(reviewsData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetReviews();
  }, []);

  useEffect(() => {
    const handleIsTutorStudent = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/lessons/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const isStudentData = await response.json();
        const isStudent = isStudentData.some(lesson => lesson.student_mail === visitor_mail);

        setIsTutorStudent(isStudent);
      } catch (error) {
        console.error(error);
      }
    };

    handleIsTutorStudent();
  }, []);

  const handleReviewAddition = () => {
    const reviewData = {
      rating: rating,
      review_text: reviewText,
      tutor_mail: email,
      student_mail: visitor_mail,
    };

    // Send POST request to add review
    fetch('http://localhost:8000/tutor/add_review', {
      method: 'POST',
      body: JSON.stringify(reviewData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        // Append the new review to the existing reviews
        setReviews(prevReviews => [...prevReviews, data]);
        setReviewText('');
      })
      .catch(error => console.error('Error adding review:', error));
  };

  const handleSendMessage = () => {
    const messageData = {
      message_text: messageToTutor,
      tutor_mail: email,
      student_mail: visitor_mail,
    };

    // Send POST request to send message to tutor
    fetch('http://localhost:8000/student/message_to_tutor', {
      method: 'POST',
      body: JSON.stringify(messageData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        console.log('Message sent:', data);
        setMessageToTutor('');
      })
      .catch(error => console.error('Error sending message:', error));
  };

  const renderStarRating = () => {
    const stars = [];
    const maxRating = 5;

    for (let i = 1; i <= maxRating; i++) {
      const starClass = i <= rating ? 'star-filled' : 'star-unfilled';

      stars.push(
        <span
          key={i}
          className={starClass}
          onClick={() => setRating(i)}
        >
          &#9733;
        </span>
      );
    }

    return stars;
  };

  return (
    <div style={containerStyle}>
      <ThemeProvider theme={theme}>
        <HeaderStyledTypography variant="h4" align="center">
          Tutor's Profile
        </HeaderStyledTypography>
        <ProfileBox>
          <ProfileImage>
            <Avatar
              style={{ width: 180, height: 180 }}
              src={profileAddress === '' ? require('../Storage/default') : require('../Storage/' + email)} />
          </ProfileImage>
          <InfoBox>
            <List>
              <ListItem style={{ margin: -5 }}>
                <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                  First Name:
                </Typography>
                <Typography variant="h6" sx={{ marginLeft: 1, }}>
                  {firstName}
                </Typography>
              </ListItem>
              <ListItem style={{ margin: -5 }}>
                <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                  Last Name:
                </Typography>
                <Typography variant="h6" sx={{ marginLeft: 1, }}>
                  {lastName}
                </Typography>
              </ListItem>
              <ListItem style={{ margin: -5 }}>
                <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                  Biography:
                </Typography>
                <Typography variant="h6" sx={{ marginLeft: 1, }}>
                  {biography === "" ? "No biography." : biography}
                </Typography>
              </ListItem>
            </List>
          </InfoBox>
          <InfoBox>
            <List>
              <ListItem>
                <TextField
                  id="message"
                  fullWidth
                  label="Message to Tutor"
                  name="message"
                  onChange={e => setMessageToTutor(e.target.value)}
                  value={messageToTutor}
                  size="small"
                />
                <Button
                  onClick={handleSendMessage}
                  sx={{ marginLeft: 1, }}
                  variant="outlined"
                  size="small"
                >
                  Send
                </Button>
              </ListItem>
              {is_tutor_student && (
                <div>
                  <ListItem>
                    <TextField
                      id="review"
                      fullWidth
                      label="Review"
                      name="review"
                      onChange={e => setReviewText(e.target.value)}
                      value={reviewText}
                      size="small"
                    />
                    <Button
                      onClick={handleReviewAddition}
                      sx={{ marginLeft: 1, }}
                      variant="outlined"
                      size="small"
                    >
                      Send
                    </Button>
                  </ListItem>
                  <ListItem>
                    {renderStarRating()}
                  </ListItem>
                </div>
              )}
            </List>
          </InfoBox>
        </ProfileBox>
        <ListBox>
          <ListItemBox>
            <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
              Courses:
            </Typography>
            {courses.length > 0 ? (
              <List>
                {courses.map((course, index) => (
                  <ListItem key={course.id}>
                    <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                      Subject:
                    </Typography>
                    <Typography variant="h6" sx={{ marginLeft: 1, }}>
                      {course.subject}
                    </Typography>
                    <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                      Price:
                    </Typography>
                    <Typography variant="h6" sx={{ marginLeft: 1, }}>
                      {course.price}
                    </Typography>
                  </ListItem>
                ))}
              </List>
            ) : (
              <Typography variant="h5" sx={{ marginLeft: 1, }}>
                No Courses!
              </Typography>
            )}
          </ListItemBox>
          <ListItemBox>
            <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
              Reviews:
            </Typography>
            {reviews.length > 0 ? (
              <List>
                {reviews.map((review, index) => (
                  <ListItem key={index}>
                    <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                      Review:
                    </Typography>
                    <Typography variant="h6" sx={{ marginLeft: 1, }}>
                      {review && review['review_text']}
                    </Typography>
                    <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                      Reviewer:
                    </Typography>
                    <Typography variant="h6" sx={{ marginLeft: 1, }}>
                      {review && review['student_mail']}
                    </Typography>
                  </ListItem>
                ))}
              </List>
            ) : (
              <Typography variant="h5" sx={{ marginLeft: 1, }}>
                No Reviews!
              </Typography>
            )}
          </ListItemBox>
        </ListBox>
      </ThemeProvider>
    </div>
  );
};

export default PublicTutor;