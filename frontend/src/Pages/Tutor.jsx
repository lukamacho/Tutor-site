import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { Typography, TextField, Button, Card, CardContent, CardHeader, Grid } from '@mui/material';

import './TutorProfile.css';

function TutorProfile() {
  const [data, setData] = useState([]);
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [biography, setBiography] = useState('');
  const [balance, setBalance] = useState(0);
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
        setBiography(tutorData['biography'])
        setProfileAddress(tutorData['profile_address']);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetTutor();
  }, []);



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
        setBalance(balance-withdrawalMoney)
      })
      .catch(error => console.error('Error requesting money withdrawal:', error));
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
            src={profileAddress === ''
              ? require("../Storage/default")
              : require("../Storage/" + email)}
            style={{ width: 120, height: 140 }} />
          <form onSubmit={handleSubmit}>
            <input name="image" type="file" onChange={changeHandler} accept=".jpeg, .png, .jpg"/>
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
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  );
}

export default TutorProfile;
