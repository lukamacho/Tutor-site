import { useState, useEffect } from 'react';
import { Link } from "react-router-dom"

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
    <div>
      <h1>Tutors</h1>
      <ul>
        {tutors.map((tutor, index) =>
          <li key={index}>
            First Name: {tutor["first_name"]};
            Last Name: {tutor["last_name"]};
            Mail: <Link to={"/tutor/" + tutor["email"]}>{tutor["email"]}</Link>;
            Biography: {tutor["biography"]};
            Profile Address: {tutor["profile_address"]};
          </li>)}
      </ul>
    </div>
  );
}