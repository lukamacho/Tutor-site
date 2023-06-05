import React from 'react';
import { useLocation } from 'react-router-dom';

export default function Student() {
  const location = useLocation();
  const email = location.state?.email;

  return (
    <div>
      <h1>Student Profile</h1>
      <p>Email: {email}</p>
      <p>Welcome to your student profile!</p>
    </div>
  );
}
