import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function Student() {
  const location = useLocation();
  const email = location.state?.email;

  const [data, setData] = useState([])
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [balance, setBalance] = useState(0)
  const [profileAddress, setProfileAddress] = useState('')

  const [newFirstName, setNewFirstName] = useState('')
  const [newLastName, setNewLastName] = useState('')
  const [newPassword, setNewPassword] = useState('')

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
        setData(data)
        console.log(data)

        setFirstName(data['first_name'])
        setLastName(data['last_name'])
        setBalance(data['balance'])
        setProfileAddress(data['profile_address'])
      } catch (error) {
        console.error(error);
      }
    };

    handleGetStudent();
  }, []);

  const handleChangeFirstName = async () => {
    try {
      const data = {
        "new_first_name": newFirstName,
      }

      const response = await fetch('http://localhost:8000/student/change_first_name/' + email, {
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

  const handleChangeLastName = async () => {
    try {
      const data = {
        "new_last_name": newLastName,
      }

      const response = await fetch('http://localhost:8000/student/change_last_name/' + email, {
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

  const handleChangePassword = async () => {
    try {
      const data = {
        "new_password": newPassword,
      }

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
  }

  const [selectedImage, setSelectedImage] = useState(null);

  const changeHandler = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSubmit = event => {
    event.preventDefault();
    const form_data = new FormData();
    form_data.append(
      "file",
      selectedImage,
      selectedImage.name
    );

    const requestOptions = {
      method: 'POST',
      body: form_data
    };
    fetch('http://localhost:8000/student/upload_profile_picture/' + email, requestOptions)
      .then(response => response.json())
      .then(function (response) {
        console.log(response)
    });
  }

  return (
    <div>
      <h1>Student Profile</h1>
      <img
        src={profileAddress === ''
          ? require("../Storage/default")
          : require("../Storage/" + email)}
        style={{ width: 120, height: 140 }} />
      <form onSubmit={handleSubmit}>
        <input name="image" type="file" onChange={changeHandler} accept=".jpeg, .png, .jpg"/>
        <button type="submit">Save</button>
      </form>
      <p>Email: {email}</p>
      <p>Welcome to your student profile!</p>
      <p>First Name: {firstName}</p>
      <p>Last Name: {lastName}</p>
      <p>Balance: {balance}</p>
      <p>Profile Address: {profileAddress}</p>
      <input
        type="text"
        value={newFirstName}
        onChange={(e) => setNewFirstName(e.target.value)}
        placeholder="new first name"
      />
      <button onClick={handleChangeFirstName}>Change First Name</button>
      <br/>
      <input
        type="text"
        value={newLastName}
        onChange={(e) => setNewLastName(e.target.value)}
        placeholder="new last name"
      />
      <button onClick={handleChangeLastName}>Change Last Name</button>
      <br/>
      <input
        type="text"
        value={newPassword}
        onChange={(e) => setNewPassword(e.target.value)}
        placeholder="new password"
      />
      <button onClick={handleChangePassword}>Change Password</button>
    </div>
  );
}
