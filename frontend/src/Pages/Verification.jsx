import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

export default function Verification() {
  const location = useLocation();
  const navigate = useNavigate();

  const [verificationCode, setVerificationCode] = useState("");
  const [verificationError, setVerificationError] = useState(false);
  const [resendLoading, setResendLoading] = useState(false);
  const [resendSuccess, setResendSuccess] = useState(false);

  const is_student = location.state?.is_student; // Access the is_student variable
  const email = location.state?.email; // Access the email variable
  const first_name = location.state?.first_name; // Access the first_name variable
  const last_name = location.state?.last_name; // Access the last_name variable
  const password = location.state?.password; // Access the password variable

  const handleVerification = async (e) => {
    e.preventDefault();

    // Compare the entered verification code with the expected code
    const expectedCode = location.state?.verificationCode;

    if (verificationCode === expectedCode) {
      const data = {
        first_name: first_name,
        last_name: last_name,
        mail: email,
        password: password,
        is_student: is_student,
      };

      try {
        const response = await fetch("http://localhost:8000/add_user", {
          method: "POST",
          body: JSON.stringify(data),
          headers: { "Content-Type": "application/json" },
        });
        const result = await response.json();
      } catch (error) {
        console.error(error);
      }

      if (is_student) {
        navigate("/student_profile", {
          state: { email, first_name, last_name, password },
        });
      } else {
        navigate("/tutor_profile", {
          state: { email, first_name, last_name, password },
        });
      }
    } else {
      // Verification unsuccessful
      setVerificationError(true);
    }
  };

  const handleResend = async () => {
    setResendLoading(true);

    // Send a request to the server to resend the verification code
        const data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "mail": email,
                    "password": password,
                    "is_student": is_student,
                }

       try {
         const response = await fetch('http://localhost:8000/sign_up', {
              method: 'POST',
              body: JSON.stringify(data),
              headers: { 'Content-Type': 'application/json' }
       });
      const result = await response.json();
      navigate('/verification', {
            state: {
              email,
              verificationCode: result.verificationCode,
              is_student,
              first_name: first_name,
              last_name: last_name,
              password
            }
          });
      setResendSuccess(true);
    } catch (error) {
      console.error(error);
    }

    setResendLoading(false);
  };

  return (
    <div>
      <h1>Verification</h1>
      <p>Enter the verification code sent to your email.</p>
      <form onSubmit={handleVerification}>
        <input
          type="text"
          placeholder="Verification code"
          value={verificationCode}
          onChange={(e) => setVerificationCode(e.target.value)}
        />
        <button type="submit">Verify</button>
      </form>
      {verificationError && <p>Incorrect verification code. Please try again.</p>}
      <button onClick={handleResend} disabled={resendLoading}>
        {resendLoading ? "Resending..." : "Resend"}
      </button>
      {resendSuccess && <p>Verification code resent successfully.</p>}
    </div>
  );
}
