import React, { useEffect, useState } from 'react';
import { useLocation, Link, useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import backgroundImage from '../Images/StudentProfileBG.png';
import { HeaderStyledTypography } from "../Components/Styles"
import Avatar from '@mui/material/Avatar';
import { theme } from "../Components/Theme"
import { ThemeProvider } from '@mui/material/styles';
import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const containerStyle = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
};

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

export const InfoBox = styled(Box)(({ theme }) => ({
  margin: 15,
  borderRadius: '10px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.4)',
  backgroundColor: 'rgba(255, 255, 255, 0.8)',
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

export const ProfileBox = styled(Box)(({ theme }) => ({
  alignItems: 'center',
  backgroundColor: 'rgba(248, 224, 255, 0)',
  borderRadius: '14px',
  display: 'flex',
  justifyContent: 'center',
  width: "100%",
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

const Student = ({ token }) => {
  let emailToken = JSON.parse(sessionStorage.getItem('email'))
  let emailStr = emailToken === null ? '' : emailToken

  const [email, setEmail] = useState(emailStr);
  const navigate = useNavigate(); // Add navigate from react-router-dom

  console.log("student token: %s and email: %s", token, email);

  const [data, setData] = useState([]);
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [balance, setBalance] = useState(0);
  const [profileAddress, setProfileAddress] = useState('');
  const [homeworks, setHomeworks] = useState([]);
  const [newFirstName, setNewFirstName] = useState('');
  const [newLastName, setNewLastName] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [newBalance, setNewBalance] = useState(0);

  const [lessons, setLessons] = useState([]);

  const [report, setReport] = useState('');

  useEffect(() => {
    const handleGetStudent = async () => {
      try {
        const response = await fetch('http://localhost:8000/student/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        setData(data);
        console.log(data);

        setFirstName(data['first_name']);
        setLastName(data['last_name']);
        setBalance(data['balance']);

        console.log("set profile address");
        setProfileAddress(data['profile_address']);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetStudent();
  }, []);

  useEffect(() => {
    const updateProfileAddress = async () => {
      console.log("profile image session storage set item")
      console.log(profileAddress)
      sessionStorage.setItem("profileImage", JSON.stringify(profileAddress));
    };

    updateProfileAddress();
  }, [profileAddress]);

  useEffect(() => {
    const handleGetLessons = async () => {
      try {
        const response = await fetch('http://localhost:8000/student/lessons/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const lessonsData = await response.json();
        setLessons(lessonsData);
        console.log(lessonsData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetLessons();
  }, []);

  useEffect(() => {
    const handleGetHomeworks = async () => {
      try {
        const response = await fetch('http://localhost:8000/student/homeworks/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const homeworksData = await response.json();
        setHomeworks(homeworksData);
        console.log(homeworksData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetHomeworks();
  }, []);

  const handleNavigateToMessages = () => {
    navigate('/student/messages', { state: { email } });
  };

  const handleChangeFirstName = async () => {
  try {
    const data = {
      new_first_name: newFirstName,
    };

    const response = await fetch('http://localhost:8000/student/change_first_name/' + email, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    const responseJson = await response.json();
    console.log(responseJson);

    // Update the state locally with the new first name
    setFirstName(newFirstName);
    // Clear the new first name input field after updating
    setNewFirstName('');
  } catch (error) {
    console.error(error);
  }
};


  const handleChangeLastName = async () => {
  try {
    const data = {
      new_last_name: newLastName,
    };

    const response = await fetch('http://localhost:8000/student/change_last_name/' + email, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    const responseJson = await response.json();
    console.log(responseJson);

    // Update the state locally with the new last name
    setLastName(newLastName);
    // Clear the new last name input field after updating
    setNewLastName('');
  } catch (error) {
    console.error(error);
  }
};


  const handleChangePassword = async () => {
    try {
      const data = {
        new_password: newPassword,
      };

      const response = await fetch('http://localhost:8000/student/change_password/' + email, {
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
  };

  const [selectedImage, setSelectedImage] = useState(null);

  const changeHandler = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const form_data = new FormData();
    form_data.append('file', selectedImage, selectedImage.name);

    const requestOptions = {
      method: 'POST',
      body: form_data,
    };

    fetch(`http://localhost:8000/student/upload_profile_picture/${email}`, requestOptions)
      .then((response) => response.json())
      .then(function (response) {
        console.log(response);
      });
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

  const handleAddBalance = async () => {
    if (newBalance > 0) {
      const data = {
        amount: newBalance,
      };

      const response = await fetch('http://localhost:8000/student/add_balance/' + email, {
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

  const handleFinishHomework = async (homework_text, tutor_mail) => {
    const data = {
      homework_text: homework_text,
      tutor_mail: tutor_mail,
      student_mail: email,
    };
    const response = await fetch('http://localhost:8000/student/finish_homework' , {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    const response2 = await response.json();
    console.log(response2);
  };

  const buyLesson = async (index) => {
    try {
      const data = {
        subject: lessons[index].subject,
        tutor_mail: lessons[index].tutor_mail,
        lesson_price: lessons[index].lesson_price,
      };

      const response = await fetch('http://localhost:8000/student/buy_lesson/' + email, {
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
  };

  return (
    <div style={containerStyle}>
      <ThemeProvider theme={theme}>
        <HeaderStyledTypography variant="h4" align="center">
          My Profile
        </HeaderStyledTypography>
        <div style={{ display: 'flex', padding: 10 }}>
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
              </List>
            </InfoBox>
            <InfoBox>
              <List>
                <ListItem>
                  <TextField
                    id="new-first-name"
                    fullWidth
                    label="New First Name"
                    name="new-first-name"
                    onChange={e => setNewFirstName(e.target.value)}
                    value={newFirstName}
                    size="small"
                  />
                  <Button
                    onClick={handleChangeFirstName}
                    sx={{ marginLeft: 1, }}
                    variant="outlined"
                    size="medium"
                  >
                    Change
                  </Button>
                </ListItem>
                <ListItem>
                  <TextField
                    id="new-last-name"
                    fullWidth
                    label="New Last Name"
                    name="new-last-name"
                    onChange={e => setNewLastName(e.target.value)}
                    value={newLastName}
                    size="small"
                  />
                  <Button
                    onClick={handleChangeLastName}
                    sx={{ marginLeft: 1, }}
                    variant="outlined"
                    size="medium"
                  >
                    Change
                  </Button>
                </ListItem>
                <ListItem>
                  <TextField
                    id="new-password"
                    fullWidth
                    label="New Password"
                    name="new-password"
                    onChange={e => setNewPassword(e.target.value)}
                    value={newPassword}
                    size="small"
                  />
                  <Button
                    onClick={handleChangePassword}
                    sx={{ marginLet: 1, }}
                    variant="outlined"
                    size="medium"
                  >
                    Change
                  </Button>
                </ListItem>
                <ListItem>
                  <input name="image" type="file" onChange={changeHandler} accept=".jpeg, .png, .jpg" />
                  <Button
                    onClick={handleSubmit}
                    sx={{ marginLet: 1, }}
                    variant="outlined"
                    size="medium"
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
                    label="New Balance"
                    onChange={e => setNewBalance(e.target.value)}
                    value={newBalance}
                    size="small"
                  />
                  <Button
                    onClick={handleAddBalance}
                    sx={{ marginLet: 1, }}
                    variant="outlined"
                    size="medium"
                  >
                    Add Balance
                  </Button>
                </ListItem>
              </List>
            </InfoBox>
          </ProfileBox>
        </div>
        <ListBox>
          <ListItemBox>
            <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
              Lessons:
            </Typography>
            {lessons.length < 1 ? (
              <Typography variant="h5" sx={{ marginLeft: 1, }}>
                No lessons!
              </Typography>
            ) : (
              <List>
                {lessons.map((lesson, index) => (
                  <ListItem key={index}>
                    Subject: {lesson['subject']}; Tutor:{' '}
                    <Link to={'http://localhost:3000/tutors/tutor/' + lesson['tutor_mail']}>{lesson['tutor_mail']}</Link>
                    Number of lessons: {lesson['number_of_lessons']}; Lesson price: {lesson['lesson_price']};
                    <Button onClick={(e) => buyLesson(index)}>Buy Lesson</Button>
                  </ListItem>
                ))}
              </List>
            )}
          </ListItemBox>
          <ListItemBox>
            <Typography variant="h4" sx={{ fontWeight: 'bold' }}>
              Homeworks:
            </Typography>
            {homeworks.length < 1 ? (
              <Typography variant="h5" sx={{ marginLeft: 1, }}>
                No homework!
              </Typography>
            ) : (
              <List>
                {homeworks.map((homework, index) => (
                  <ListItem key={index}>
                    {homework.homework_text}
                    <button onClick={() => handleFinishHomework(homework.homework_text,homework.tutor_mail)}>Finish</button>
                  </ListItem>
                ))}
              </List>
            )}
          </ListItemBox>
        </ListBox>
      </ThemeProvider>
    </div>
  );
}

Student.propTypes = {
  token: PropTypes.string.isRequired,
};

export default Student;