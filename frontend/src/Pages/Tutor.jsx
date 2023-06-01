import React from 'react';
import { useLocation } from 'react-router-dom';

export default function Tutor() {
  const location = useLocation();
  const email = location.state?.email;

  return (
    <div>
      <h1>Tutor Profile</h1>
      <p>Email: {email}</p>
      <p>Welcome to your tutor profile!</p>
    </div>
  );
}
