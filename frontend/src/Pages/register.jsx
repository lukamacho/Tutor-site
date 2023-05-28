import React, { useState } from "react";


function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isTutor, setIsTutor] = useState(false);


  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleTutorClick = () => {
    setIsTutor(true);
  };

  const handleStudentClick = () => {
    setIsTutor(false);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Email: ${email}, Password: ${password}, isTutor: ${isTutor}`);
    // You can add your registration logic here

  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Email:
          <input type="email" value={email} onChange={handleEmailChange} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={handlePasswordChange} />
        </label>
        <br />
        <label>
          Register as:
          <br />
          <button type="button" onClick={handleTutorClick} style={{ marginRight: 10 }}>
            Tutor
          </button>
          <button type="button" onClick={handleStudentClick}>
            Student
          </button>
        </label>
        <br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
