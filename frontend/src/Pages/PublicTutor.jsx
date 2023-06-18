import { useParams } from "react-router-dom";
import { useState, useEffect } from 'react';

const PublicTutor= () => {
  const {email} = useParams();

  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [biography, setBiography] = useState('');
  const [profileAddress, setProfileAddress] = useState('');

  const [courses, setCourses] = useState([])

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
        setBiography(tutorData['biography'])
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
        setCourses(coursesData)
        console.log(coursesData)
      } catch (error) {
        console.error(error);
      }
    };

    handleGetCourses();
  }, []);

  return (
    <div>
      <h1>Tutor's Public Profile</h1>
      <img
        src={profileAddress === ''
          ? require("../Storage/default")
          : require("../Storage/" + email)}
        style={{ width: 120, height: 140 }} />
      <p>First Name: {firstName}</p>
      <p>Last Name: {lastName}</p>
      <p>Biography: {biography}</p>
      <p>Profile Address: {profileAddress}</p>
      <br />
      <h1>Courses:</h1>
      <ul>
        {courses.map((course, index) =>
          <li key={index}>
            Subject: {course["subject"]};
            Lesson price: {course["price"]};
          </li>
        )}
      </ul>
    </div>
  );
}

export default PublicTutor;
