import React, { useEffect, useState } from 'react';
import { useLocation, Link, useNavigate } from 'react-router-dom';
import { Typography, TextField, Button, Card, CardContent, CardHeader, Grid } from '@mui/material';
import PropTypes from 'prop-types';
import backgroundImage from '../Images/TutorProfileBG.png';
import { theme } from "../Components/Theme"
import { ThemeProvider } from '@mui/material/styles';
import './TutorProfile.css';
import { HeaderStyledTypography } from "../Components/Styles"
import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';

const containerStyle = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
};

export const ProfileBox = styled(Box)(({ theme }) => ({
  alignItems: 'center',
  backgroundColor: 'rgba(248, 224, 255, 0.2)',
  borderRadius: '14px',
  display: 'flex',
  justifyContent: 'center',
  width: "100%",
}));

export const InfoBox = styled(Box)(({ theme }) => ({
  margin: 15,
  borderRadius: '10px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.4)',
  backgroundColor: 'rgba(255, 255, 255, 0.8)',
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
  backgroundColor: 'rgba(255, 255, 255, 0.2)',
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

const Tutor = ({ token }) => {
  let emailToken = JSON.parse(sessionStorage.getItem('email'))
  let emailStr = emailToken === null ? '' : emailToken

  const [email, setEmail] = useState(emailStr);

  console.log("tutor token: %s and email: %s", token, email);

  const [data, setData] = useState([]);
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [biography, setBiography] = useState('');
  const [courseName, setCourseName] = useState('');
  const [coursePrice, setCoursePrice] = useState(0);
  const [balance, setBalance] = useState(0);
  const [courses, setCourses] = useState([]);
  const [tutorStudents, setTutorStudents] = useState([]);
  const [homeworkData, setHomeworkData] = useState({});
  const [report, setReport] = useState('');
  const navigate = useNavigate();
  const [profileAddress, setProfileAddress] = useState('');
  const [withdrawalMoney, setWithdrawalMoney] = useState('');
  const [profilePicture, setProfilePicture] = useState(null);
  const [newBio, setNewBio] = useState('');

  const location = useLocation();

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
        setData(tutorData);
        setFirstName(tutorData['first_name']);
        setLastName(tutorData['last_name']);
        setBalance(tutorData['balance']);
        setBiography(tutorData['biography']);
        setProfileAddress(tutorData['profile_address']);
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
        console.log(coursesData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetCourses();
  }, []);

  useEffect(() => {
    const handleGetTutorStudents = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/students/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const tutorStudentsData = await response.json();
        setTutorStudents(tutorStudentsData);
        console.log(tutorStudentsData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetTutorStudents();
  }, []);

    const handleAddHomework = (studentId, studentMail) => {
    // Get the homework data entered for the student
    const homework = homeworkData[studentId];

    const requestData = {
      tutor_mail: email,
      student_mail: studentMail,
      homework: homework,
    };

    fetch('http://localhost:8000/tutor/add_homework', {
      method: 'POST',
      body: JSON.stringify(requestData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        // Process the response as needed
        console.log('Add homework response:', data);

        // Clear the homework data for the student
        setHomeworkData(prevData => ({
          ...prevData,
          [studentId]: '',
        }));
      })
      .catch(error => console.error('Error adding homework:', error));
  };
  const handleNavigateToMessages = () => {
    navigate('/tutor/messages', { state: { email } });
  };

  const handleHomeworkChange = (studentId, value) => {
    setHomeworkData(prevData => ({
      ...prevData,
      [studentId]: value,
    }));
  };

  const handleWithdrawalRequest = () => {
  // Convert withdrawalMoney to a number (since it is read from an input field)
  const withdrawalAmount = parseFloat(withdrawalMoney);

  if (isNaN(withdrawalAmount)) {
    // If the withdrawal amount is not a valid number, display an error or handle it appropriately.
    console.error('Withdrawal amount is not a valid number.');
    return;
  }

  if (balance >= withdrawalAmount) {
    const requestData = {
      tutor_mail: email,
      amount: withdrawalAmount,
    };

    // Send POST request to request money withdrawal
    fetch(`http://localhost:8000/withdrawal_request`, {
      method: 'POST',
      body: JSON.stringify(requestData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        // Process the response as needed
        console.log('Withdrawal request response:', data);
        setBalance(balance - withdrawalAmount);
      })
      .catch(error => console.error('Error requesting money withdrawal:', error));
  } else {
    // Handle the case where the balance is less than the withdrawal amount
    console.error('Insufficient balance for withdrawal.');
    // You can display an error message or take any other action here.
  }
};


   const handleSendReportToAdmin = async () => {
    if (report !== '') {
      const data = {
        report: report,
      };

      const response = await fetch('http://localhost:8000/admin/report_to_admin/' + email, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const response2 = await response.json();
      console.log(response2);
    }
  };

  const handleBioChange = async () => {
  try {
    const bioData = {
      tutor_mail: email,
      new_bio: newBio,
    };

    // Send POST request to update tutor's bio
    const response = await fetch('http://localhost:8000/tutor/change_bio', {
      method: 'POST',
      body: JSON.stringify(bioData),
      headers: {
        'Content-Type': 'application/json',
      },
    });

    const responseJson = await response.json();
    console.log(responseJson);

    // Update the state locally with the new biography
    setBiography(newBio);
    // Clear the new bio input field after updating
    setNewBio('');
  } catch (error) {
    console.error('Error updating bio:', error);
  }
};


  const handleCourseAddition = () => {
    const courseData = {
      tutor_mail: email,
      course_name: courseName,
      course_price: coursePrice,
    };

    // Send POST request to update tutor's course information
    fetch(`http://localhost:8000/tutor/add_course`, {
      method: 'POST',
      body: JSON.stringify(courseData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        setCourseName('');
        setCoursePrice(0);
      })
      .catch(error => console.error('Error adding course:', error));
  };

//   const handleCourseDeletion = course => {
//     const courseData = {
//       tutor_mail: course.tutor_mail,
//       course_name: course.subject,
//     };
//
//     // Send DELETE request to delete the course
//     fetch(`http://localhost:8000/tutor/delete_course`, {
//       method: 'DELETE',
//       body: JSON.stringify(courseData),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     })
//       .then(response => response.json())
//       .catch(error => console.error('Error deleting course:', error));
//   };
  const [selectedImage, setSelectedImage] = useState(null);

  const changeHandler = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSubmit = event => {
  event.preventDefault();
  const form_data = new FormData();
  form_data.append("file", selectedImage, selectedImage.name);

  const requestOptions = {
    method: 'POST',
    body: form_data
  };

  fetch(`http://localhost:8000/tutor/upload_profile_picture/${email}`, requestOptions)
    .then(response => response.json())
    .then(function (response) {
      console.log(response);
    });
};

const handleCourseDeletion = (course) => {
    const courseData = {
      tutor_mail: course.tutor_mail,
      course_name: course.subject,
    };
  // Send DELETE request to delete the course
  fetch(`http://localhost:8000/tutor/delete_course`, {
    method: 'DELETE',
    body: JSON.stringify(courseData),
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then(response => response.json())

    .catch(error => console.error('Error deleting course:', error));
};

  useEffect(() => {
    sessionStorage.setItem("email", JSON.stringify(email));
    sessionStorage.setItem("isStudent", JSON.stringify(false));
    sessionStorage.setItem("profileImage", JSON.stringify(profileAddress));
  }, [email]);

  return (
    <div style={containerStyle}>
      <ThemeProvider theme={theme}>
        <HeaderStyledTypography variant="h4" align="center">
          My Profile
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
                  Email:
                </Typography>
                <Typography variant="h6" sx={{ marginLeft: 1, }}>
                  {email}
                </Typography>
              </ListItem>
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
                  Balance:
                </Typography>
                <Typography variant="h6" sx={{ marginLeft: 1, }}>
                  {balance}
                </Typography>
              </ListItem>
              <ListItem style={{ margin: -5 }}>
                <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                  Biography:
                </Typography>
                <Typography variant="h6" sx={{ marginLeft: 1, }}>
                  {biography}
                </Typography>
              </ListItem>
            </List>
          </InfoBox>
          <InfoBox>
            <List>
              <ListItem>
                <TextField
                  id="new-biography"
                  fullWidth
                  label="New Biography"
                  name="new-biography"
                  onChange={e => setNewBio(e.target.value)}
                  value={newBio}
                  size="small"
                  multiline
                  rows={4}
                />
                <Button
                  onClick={handleBioChange}
                  sx={{ marginLeft: 1, }}
                  variant="outlined"
                  size="small"
                >
                  Change
                </Button>
              </ListItem>
              <ListItem>
                <TextField
                  id="withdrawal-amount"
                  fullWidth
                  label="Withdrawal Amount"
                  name="withdrawal-amount"
                  onChange={e => setWithdrawalMoney(e.target.value)}
                  value={withdrawalMoney}
                  size="small"
                />
                <Button
                  onClick={handleWithdrawalRequest}
                  sx={{ marginLeft: 1, }}
                  variant="outlined"
                  size="small"
                >
                  Request
                </Button>
              </ListItem>
              <ListItem>
                <input name="image" type="file" onChange={changeHandler} accept=".jpeg, .png, .jpg" />
                <Button
                  onClick={handleSubmit}
                  sx={{ marginLet: 1, }}
                  variant="outlined"
                  size="small"
                >
                  Save
                </Button>
              </ListItem>
            </List>
          </InfoBox>
          <InfoBox>
            <List>
              <ListItem>
                <Button
                  onClick={handleNavigateToMessages}
                  sx={{ marginLet: 1, }}
                  variant="outlined"
                  size="medium"
                >
                  Messages
                </Button>
                </ListItem>
                <ListItem>
                  <TextField
                    label="My Report"
                    onChange={e => setReport(e.target.value)}
                    value={report}
                    size="small"
                  />
                  <Button
                    onClick={handleSendReportToAdmin}
                    sx={{ marginLet: 1, }}
                    variant="outlined"
                    size="medium"
                  >
                    Send to Admin
                  </Button>
              </ListItem>
              <ListItem>
                <TextField
                  label="Course Name"
                  value={courseName}
                  onChange={event => setCourseName(event.target.value)}
                  variant="outlined"
                  fullWidth
                  size="small"
                />
                <TextField
                  label="Course Price"
                  value={coursePrice}
                  onChange={event => setCoursePrice(event.target.value)}
                  variant="outlined"
                  fullWidth
                  size="small"
                />
                <Button variant="outlined" color="primary" onClick={handleCourseAddition}>
                  Add course
                </Button>
              </ListItem>
            </List>
          </InfoBox>
        </ProfileBox>
        <ListBox>
          <ListItemBox>
            <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
              Courses:
            </Typography>
            {courses.length > 0 ?
              (
                <List>
                  {courses.map(course => (
                    <ListItem key={course.id}>
                      <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                        Subject:
                      </Typography>
                      <Typography variant="h6" sx={{ marginLeft: 1, }}>
                        {course.subject}
                      </Typography>
                      <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                        Tutor:
                      </Typography>
                      <Typography variant="h6" sx={{ marginLeft: 1, }}>
                        {course.tutor_mail}
                      </Typography>
                      <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                        Price:
                      </Typography>
                      <Typography variant="h6" sx={{ marginLeft: 1, }}>
                        {course.price}
                      </Typography>
                      <Button
                        variant="contained"
                        color="secondary"
                        onClick={() => handleCourseDeletion(course, course.id)}
                      >
                        Delete
                      </Button>
                    </ListItem>
                  ))}
                </List>
              ) : (
                <Typography variant="h5" sx={{ marginLeft: 1, }}>
                  No Courses!
                </Typography>
              )
            }
          </ListItemBox>
          <ListItemBox>
            <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
              Students:
            </Typography>
            {tutorStudents.length > 0 ?
              (
                <List>
                  {tutorStudents.map(student =>
                    (
                      <ListItem key={student.id}>
                        <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                          First Name:
                        </Typography>
                        <Typography variant="h6" sx={{ marginLeft: 1, }}>
                          {student.first_name}
                        </Typography>
                        <Typography variant="h6" sx={{ fontWeight: 'bold' }}>
                          Last Name:
                        </Typography>
                        <Typography variant="h6" sx={{ marginLeft: 1, }}>
                          {student.last_name}
                        </Typography>
                        <TextField
                          label="Homework"
                          variant="outlined"
                          fullWidth
                          value={homeworkData[student.id] || ''}
                          onChange={(e) =>
                            handleHomeworkChange(student.id, e.target.value)
                          }
                        />
                        <Button
                          variant="contained"
                          color="primary"
                          onClick={() => handleAddHomework(student.id,student.email)}
                        >
                          Add Homework
                        </Button>
                      </ListItem>
                    ))
                  }
                </List>
              ) : (
                <Typography variant="h5" sx={{ marginLeft: 1, }}>
                  No Students!
                </Typography>
              )
            }
          </ListItemBox>
        </ListBox>
      </ThemeProvider>
    </div>
  );
}

Tutor.propTypes = {
  token: PropTypes.string.isRequired,
};

export default Tutor;