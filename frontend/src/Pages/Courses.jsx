import { useState, useEffect } from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Course from "../Components/Course"

export default function Courses() {
  const email = localStorage.getItem("email")
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
      <List>
        {courses.map((course, index) =>
          <ListItem key={index}>
            <Course
              subject={course["subject"]}
              tutor_mail={course["tutor_mail"]}
              price={course["price"]}/>
          </ListItem>)}
      </List>
    </div>
  );
}