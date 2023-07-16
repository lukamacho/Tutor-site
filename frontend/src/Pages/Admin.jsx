import React, { useState, useEffect } from 'react';
import './Admin.css';

const Admin = () => {
  const [studentMail, setStudentMail] = useState('');
  const [tutorMail, setTutorMail] = useState('');
  const [tutorCommissionMail, setTutorCommissionMail] = useState('');
  const [tutorDecreaseMail, setTutorDecreaseMail] = useState('');
  const [studentIncreaseMail, setStudentIncreaseMail] = useState('');
  const [studentIncreaseAmount, setStudentIncreaseAmount] = useState(0);
  const [tutorDecreaseAmount, setTutorDecreaseAmount] = useState(0);
  const [studentDeleteRequested, setStudentDeleteRequested] = useState(false);
  const [tutorDeleteRequested, setTutorDeleteRequested] = useState(false);
  const [tutorCommissionRequested, setTutorCommissionRequested] = useState(false);
  const [tutorDecreaseRequested, setTutorDecreaseRequested] = useState(false);
  const [studentIncreaseRequested, setStudentIncreaseRequested] = useState(false);
  const [tutorScore, setTutorScore] = useState(0);
  const [tutorScoreOptions, setTutorScoreOptions] = useState([]);
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

    const handleDeleteStudent = async () => {
      try {
        const response = await fetch('http://localhost:8000/admin/delete_student', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ student_mail: studentMail }),
        });

        if (!response.ok) {
          throw new Error('Delete request failed');
        }

        const data = await response.json();
        console.log(data);

        if (data.message === 'Student deleted successfully') {
          setSuccessMessage('Student deleted successfully.');
          setErrorMessage('');
        } else {
          setErrorMessage('Failed to delete student.');
          setSuccessMessage('');
        }
      } catch (error) {
        console.error(error);
        setErrorMessage('Failed to delete student.');
        setSuccessMessage('');
      } finally {
        setStudentDeleteRequested(false);
      }
    };


  const handleDeleteTutor = async () => {
    try {
      const response = await fetch('http://localhost:8000/admin/delete_tutor', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tutor_mail: tutorMail }),
      });

      if (!response.ok) {
        throw new Error('Delete request failed');
      }

      const data = await response.json();
      console.log(data);
       if (data.message === 'Tutor deleted successfully') {
          setSuccessMessage('Tutor deleted successfully.');
          setErrorMessage('');
        } else {
          setErrorMessage('Failed to delete tutor.');
          setSuccessMessage('');
        }
    } catch (error) {
      setErrorMessage('Operation failed.');
      setSuccessMessage('')
      console.error(error);
    } finally {
      setTutorDeleteRequested(false);
    }
  };

  const handleCommissionTutor = async () => {
    try {
      const response = await fetch('http://localhost:8000/admin/commission_pct', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tutor_mail: tutorCommissionMail }),
      });

      if (!response.ok) {
        throw new Error('Commission request failed');
      }

      const data = await response.json();
      console.log(data);
      if (data.message === 'Commission_pct decreased successfully') {
          setSuccessMessage('Commission_pct decreased successfully.');
          setErrorMessage('');
        } else {
          setErrorMessage('Failed to decrease tutor commission_pct.');
          setSuccessMessage('');
        }
    } catch (error) {
      console.error(error);
      setErrorMessage('Operation failed.');
      setSuccessMessage('');
    } finally {
      setTutorCommissionRequested(false);
    }
  };

  const handleTutorDecreaseBalance = async () => {
    const data = {
      tutor_mail: tutorDecreaseMail,
      amount: tutorDecreaseAmount,
    };

    try {
      const response = await fetch('http://localhost:8000/admin/decrease_tutor_balance', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        throw new Error('Tutor decrease balance request failed');
      }


      const result = await response.json();
      console.log(result);
       if (result.message === 'Balance decreased successfully.') {
          setSuccessMessage('Tutor balance decreased successfully.');
          setErrorMessage('');
        } else {
          setErrorMessage('Failed to decrease tutor balance.');
          setSuccessMessage('');
      }
    } catch (error) {
      console.error(error);
      setErrorMessage('Operation failed.');
    } finally {
      setTutorDecreaseRequested(false);
    }
  };

  const handleStudentIncreaseBalance = async () => {
    const data = {
      student_mail: studentIncreaseMail,
      amount: studentIncreaseAmount,
    };

    try {
      const response = await fetch('http://localhost:8000/admin/increase_student_balance', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        throw new Error('Student increase balance request failed');
      }

      const result = await response.json();
      console.log(result);

      if (result.message === 'Balance added successfully.') {
          setSuccessMessage('Student balance increased successfully.');
          setErrorMessage('');
        } else {
          setErrorMessage('Failed to increase student balance.');
          setSuccessMessage('');
      }

    } catch (error) {
      console.error(error);
      setErrorMessage('Operation failed.');
      setSuccessMessage('')
    } finally {
      setStudentIncreaseRequested(false);
    }
  };

  const handleTutorScoreButtonClick = async () => {
    const data = {
      tutor_mail: tutorMail,
      score: tutorScore,
    };

    try {
      const response = await fetch('http://localhost:8000/admin/score_tutor', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        throw new Error('Tutor score request failed');
      }

      const result = await response.json();
      console.log(result);
       if (result.message === 'Tutor evaluated successfully.') {
          setSuccessMessage('Tutor evaluated successfully.');
          setErrorMessage('');
        } else {
          setErrorMessage('Failed to evaluate tutor.');
          setSuccessMessage('');
      }
    } catch (error) {
      console.error(error);
      setErrorMessage('Operation failed.');
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

  useEffect(() => {
    if (tutorDecreaseRequested) {
      handleTutorDecreaseBalance();
    }
  }, [tutorDecreaseRequested]);

  useEffect(() => {
    if (studentIncreaseRequested) {
      handleStudentIncreaseBalance();
    }
  }, [studentIncreaseRequested]);

  const handleStudentMailChange = (event) => {
    setStudentMail(event.target.value);
  };

  const handleTutorMailChange = (event) => {
    setTutorMail(event.target.value);
  };

  const handleTutorCommissionMailChange = (event) => {
    setTutorCommissionMail(event.target.value);
  };

  const handleTutorDecreaseMailChange = (event) => {
    setTutorDecreaseMail(event.target.value);
  };

  const handleTutorDecreaseAmountChange = (event) => {
    setTutorDecreaseAmount(event.target.value);
  };

  const handleStudentIncreaseMailChange = (event) => {
    setStudentIncreaseMail(event.target.value);
  };

  const handleStudentIncreaseAmountChange = (event) => {
    setStudentIncreaseAmount(event.target.value);
  };

  const handleTutorScoreChange = (event) => {
    setTutorScore(event.target.value);
  };

  const handleStudentDeleteButtonClick = () => {
    setSuccessMessage('');
    setErrorMessage('');
    setStudentDeleteRequested(true);
  };

  const handleTutorDeleteButtonClick = () => {
    setSuccessMessage('');
    setErrorMessage('');
    setTutorDeleteRequested(true);
  };

  const handleTutorCommissionButtonClick = () => {
    setSuccessMessage('');
    setErrorMessage('');
    setTutorCommissionRequested(true);
  };

  const handleTutorDecreaseBalanceButtonClick = () => {
    setSuccessMessage('');
    setErrorMessage('');
    setTutorDecreaseRequested(true);
  };

  const handleStudentIncreaseButtonClick = () => {
    setSuccessMessage('');
    setErrorMessage('');
    setStudentIncreaseRequested(true);
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
      <div className="decrease_tutor_balance">
        <input
          type="text"
          value={tutorDecreaseMail}
          onChange={handleTutorDecreaseMailChange}
          placeholder="Enter tutor email"
        />
        <input
          type="text"
          value={tutorDecreaseAmount}
          onChange={handleTutorDecreaseAmountChange}
          placeholder="Enter decrease amount"
        />
        <button onClick={handleTutorDecreaseBalanceButtonClick}>Decrease Tutor Balance</button>
      </div>
      <div className="increase_student_balance">
        <input
          type="text"
          value={studentIncreaseMail}
          onChange={handleStudentIncreaseMailChange}
          placeholder="Enter student email"
        />
        <input
          type="text"
          value={studentIncreaseAmount}
          onChange={handleStudentIncreaseAmountChange}
          placeholder="Enter increase amount"
        />
        <button onClick={handleStudentIncreaseButtonClick}>Increase Student balance</button>
      </div>
      <div className="evaluate_tutor">
        <input
          type="text"
          value={tutorMail}
          onChange={handleTutorMailChange}
          placeholder="Enter tutor email"
        />
        <select value={tutorScore} onChange={handleTutorScoreChange}>
          {Array.from(Array(101).keys()).map((score) => (
            <option key={score} value={score}>
              {score}
            </option>
          ))}
        </select>
        <button onClick={handleTutorScoreButtonClick}>Evaluate Tutor</button>
      </div>
      <div className="message-container">
        <span>{successMessage}</span>
        <span>{errorMessage}</span>
      </div>
    </div>
  );
};

export default Admin;
