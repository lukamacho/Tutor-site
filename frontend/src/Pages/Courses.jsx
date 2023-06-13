import { useState, useEffect } from 'react';
import { Link } from "react-router-dom"

export default function Courses() {
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

  return (
    <div>
      <h1>Courses</h1>
      <ul>
        {courses.map((course, index) =>
          <li key={index}>
            Subject: {course["subject"]};
            Tutor: <Link to={"/tutor/" + course["tutor_mail"]}>{course["tutor_mail"]}</Link>;
            Price: {course["price"]};
          </li>)}
      </ul>
    </div>
  );
}