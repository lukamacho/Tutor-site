import React, { useState, useEffect } from 'react';
import './Admin.css';

const Admin = () => {
  const [studentMail, setStudentMail] = useState('');
  const [tutorMail, setTutorMail] = useState('');
  const [tutorCommissionMail, setTutorCommissionMail] = useState('');
  const [studentDeleteRequested, setStudentDeleteRequested] = useState(false);
  const [tutorDeleteRequested, setTutorDeleteRequested] = useState(false);
  const [tutorCommissionRequested, setTutorCommissionRequested] = useState(false);

  const handleDeleteStudent = async () => {
    try {
      const response = await fetch('http://localhost:8000/admin/delete_student', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ student_mail: studentMail }), // Replace with your data
      });

      if (!response.ok) {
        throw new Error('Delete request failed');
      }
      // Handle the response
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    } finally {
      setStudentDeleteRequested(false); // Reset the deleteRequested flag
    }
  };
  const handleDeleteTutor = async () => {
    try {
      const response = await fetch('http://localhost:8000/admin/delete_tutor', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tutor_mail: tutorMail }), // Replace with your data
      });

      if (!response.ok) {
        throw new Error('Delete request failed');
      }
      // Handle the response
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    } finally {
      setTutorDeleteRequested(false); // Reset the deleteRequested flag
    }
  };
  const handleCommissionTutor = async () => {
    try {
      const response = await fetch('http://localhost:8000/admin/commission_pct', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tutor_mail: tutorCommissionMail }), // Replace with your data
      });

      if (!response.ok) {
        throw new Error('Commission request failed');
      }
      // Handle the response
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    } finally {
      setTutorCommissionRequested(false); // Reset the deleteRequested flag
    }
  };
  useEffect(() => {
    if (studentDeleteRequested) {
      handleDeleteStudent();
    }
  }, [studentDeleteRequested]);

  useEffect(() => {
    if (tutorDeleteRequested) {
      handleDeleteTutor();
    }
  }, [tutorDeleteRequested]);

   useEffect(() => {
    if (tutorCommissionRequested) {
      handleCommissionTutor();
    }
  }, [tutorCommissionRequested]);

  const handleStudentMailChange = (event) => {
    setStudentMail(event.target.value);
  };
  const handleTutorMailChange = (event) => {
    setTutorMail(event.target.value);
  };
  const handleTutorCommissionMailChange = (event) => {
    setTutorCommissionMail(event.target.value);
  };

  const handleStudentDeleteButtonClick = () => {
    setStudentDeleteRequested(true);
  };
  const handleTutorDeleteButtonClick = () => {
    setTutorDeleteRequested(true);
  };
  const handleTutorCommissionButtonClick = () => {
    setTutorCommissionRequested(true);
  };
  return (
    <div className="admin-parts">
      <h1>Admin functionality</h1>
      <div className="delete-student-container">
        <input
          type="text"
          value={studentMail}
          onChange={handleStudentMailChange}
          placeholder="Enter student email"
        />
        <button onClick={handleStudentDeleteButtonClick}>Delete Student</button>
      </div>
      <div className="delete-tutor-container">
        <input
          type="text"
          value={tutorMail}
          onChange={handleTutorMailChange}
          placeholder="Enter tutor email"
        />
        <button onClick={handleTutorDeleteButtonClick}>Delete Tutor</button>
      </div>
      <div className="change-tutor-commission_pct">
        <input
          type="text"
          value={tutorCommissionMail}
          onChange={handleTutorCommissionMailChange}
          placeholder="Enter tutor email"
        />
        <button onClick={handleTutorCommissionButtonClick}>Change tutor commission_pct</button>
      </div>
    </div>
  );
};

export default Admin;
