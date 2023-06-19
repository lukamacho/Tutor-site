import { useState, useEffect } from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import IconButton from '@mui/material/IconButton';
import AddBoxIcon from '@mui/icons-material/AddBox';
import Course from "../Components/Course"

export default function Courses() {
  const email = JSON.parse(localStorage.getItem("email"))
  const isStudent = JSON.parse(localStorage.getItem("isStudent"))
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

  const handleBuyLesson = async (course) => {
    try {
      const data = {
        "subject": course.subject,
        "tutor_mail": course.tutor_mail,
        "lesson_price": course.price,
      }

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
  }

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
            <IconButton color="primary" onClick={(e) => handleBuyLesson(course)} disabled={!isStudent}>
              <AddBoxIcon />
            </IconButton>
          </ListItem>)}
      </List>
    </div>
  );
}