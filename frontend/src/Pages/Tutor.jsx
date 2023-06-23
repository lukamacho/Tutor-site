import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { Typography, TextField, Button, Card, CardContent, CardHeader, Grid } from '@mui/material';

import './TutorProfile.css';

function TutorProfile() {
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

  const [profileAddress, setProfileAddress] = useState('');
  const [withdrawalMoney, setWithdrawalMoney] = useState('');
  const [profilePicture, setProfilePicture] = useState(null);
  const [newBio, setNewBio] = useState('');

  const location = useLocation();
  const email = location.state?.email;

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

  const handleHomeworkChange = (studentId, value) => {
    setHomeworkData(prevData => ({
      ...prevData,
      [studentId]: value,
    }));
  };

  const handleWithdrawalRequest = () => {
    const requestData = {
      tutor_mail: email,
      amount: withdrawalMoney,
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
        setBalance(balance - withdrawalMoney);
      })
      .catch(error => console.error('Error requesting money withdrawal:', error));
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

  const handleBioChange = () => {
    const bioData = {
      tutor_mail: email,
      new_bio: newBio,
    };

    // Send POST request to update tutor's bio
    fetch(`http://localhost:8000/tutor/change_bio`, {
      method: 'POST',
      body: JSON.stringify(bioData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        setNewBio(''); // Clear the newBio state
      })
      .catch(error => console.error('Error updating bio:', error));
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

  const handleCourseDeletion = course => {
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

  return (
    <div>
      <Typography variant="h1" gutterBottom>
        Tutor Profile
      </Typography>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                First Name: {firstName}
              </Typography>
              <Typography variant="h6" gutterBottom>
                Last Name: {lastName}
              </Typography>
              <Typography variant="h6" gutterBottom>
                Email: {email}
              </Typography>
              <Typography variant="h6" gutterBottom>
                Balance: {balance}
              </Typography>
              <Typography variant="h6" gutterBottom>
                Biography: {biography}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} sm={6}>
          <img
            src={
              profileAddress === ''
                ? require('../Storage/default')
                : require('../Storage/' + email)
            }
            style={{ width: 120, height: 140 }}
          />
          <form onSubmit={handleSubmit}>
            <input
              name="image"
              type="file"
              onChange={changeHandler}
              accept=".jpeg, .png, .jpg"
            />
            <button type="submit">Save</button>
          </form>
          <Card>
            <CardHeader title="Edit Bio" />
            <CardContent>
              <TextField
                value={newBio}
                onChange={event => setNewBio(event.target.value)}
                multiline
                rows={4}
                variant="outlined"
                fullWidth
              />
              <Button variant="contained" color="primary" onClick={handleBioChange}>
                Save Bio
              </Button>
              <TextField
                label="Withdrawal Amount"
                value={withdrawalMoney}
                onChange={event => setWithdrawalMoney(event.target.value)}
                variant="outlined"
                fullWidth
              />
              <Button variant="contained" color="primary" onClick={handleWithdrawalRequest}>
                Request Money Withdrawal
              </Button>
              <TextField
                label="Course name"
                value={courseName}
                onChange={event => setCourseName(event.target.value)}
                variant="outlined"
                fullWidth
              />
              <TextField
                label="Course price"
                value={coursePrice}
                onChange={event => setCoursePrice(event.target.value)}
                variant="outlined"
                fullWidth
              />
              <Button variant="contained" color="primary" onClick={handleCourseAddition}>
                Add course
              </Button>
              <ul>
                {courses.length > 0 ? (
                  courses.map(course => (
                    <li key={course.id}>
                      <span>Subject: {course.subject}</span>
                      <span>Tutor: {course.tutor_mail}</span>
                      <span>Course price: {course.price}</span>
                      <Button
                        variant="contained"
                        color="secondary"
                        onClick={() => handleCourseDeletion(course, course.id)}
                      >
                        Delete
                      </Button>
                    </li>
                  ))
                ) : (
                  <li>No courses available</li>
                )}
              </ul>
            </CardContent>
          </Card>
          <Card>
            <CardHeader title="My Students" />
            <CardContent>
              {tutorStudents.length > 0 ? (
                <ul>
                  {tutorStudents.map(student => (
                    <li key={student.id}>
                      <span>First name: {student.first_name}</span>
                      <span>Last name: {student.last_name}</span>
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
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No students</p>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
      <h4>Contact Admin</h4>
      <input
        type="text"
        value={report}
        onChange={(e) => setReport(e.target.value)}
        placeholder="my report"
      />
      <button onClick={handleSendReportToAdmin}>Send to Admin</button>
    </div>
  );
}

export default TutorProfile;
