import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import './Styles.css'

const PublicTutor = () => {
  const { email } = useParams();
  const visitor_mail = JSON.parse(localStorage.getItem('email'));

  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [biography, setBiography] = useState('');
  const [profileAddress, setProfileAddress] = useState('');

  const [courses, setCourses] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [reviewText, setReviewText] = useState('');
  const [is_tutor_student, setIsTutorStudent] = useState(false);
  const [rating, setRating] = useState(0); // New state for star rating

  const [messageToTutor, setMessageToTutor] = useState('');

  useEffect(() => {
    const handleGetTutor = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const tutorData = await response.json();
        setFirstName(tutorData['first_name']);
        setLastName(tutorData['last_name']);
        setBiography(tutorData['biography']);
        setProfileAddress(tutorData['profile_address']);
        setIsTutorStudent(tutorData['is_tutor_student']); // Retrieve the is_tutor_student flag
      } catch (error) {
        console.error(error);
      }
    };
    handleGetTutor();
  }, []);

  useEffect(() => {
    const handleGetCourses = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/courses/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const coursesData = await response.json();
        setCourses(coursesData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetCourses();
  }, []);

  useEffect(() => {
    const handleGetReviews = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/reviews/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const reviewsData = await response.json();
        setReviews(reviewsData);
      } catch (error) {
        console.error(error);
      }
    };

    handleGetReviews();
  }, []);

  useEffect(() => {
    const handleIsTutorStudent = async () => {
      try {
        const response = await fetch('http://localhost:8000/tutor/lessons/' + email, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const isStudentData = await response.json();
        const isStudent = isStudentData.some(lesson => lesson.student_mail === visitor_mail);

        setIsTutorStudent(isStudent);
      } catch (error) {
        console.error(error);
      }
    };

    handleIsTutorStudent();
  }, []);

  const handleReviewAddition = () => {
    const reviewData = {
      rating: rating,
      review_text: reviewText,
      tutor_mail: email,
      student_mail: visitor_mail,
    };

    // Send POST request to add review
    fetch('http://localhost:8000/tutor/add_review', {
      method: 'POST',
      body: JSON.stringify(reviewData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        // Append the new review to the existing reviews
        setReviews(prevReviews => [...prevReviews, data]);
        setReviewText('');
      })
      .catch(error => console.error('Error adding review:', error));
  };

  const handleSendMessage = () => {
    const messageData = {
      message_text: messageToTutor,
      tutor_mail: email,
      student_mail: visitor_mail,
    };

    // Send POST request to send message to tutor
    fetch('http://localhost:8000/student/message_to_tutor', {
      method: 'POST',
      body: JSON.stringify(messageData),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => response.json())
      .then(data => {
        console.log('Message sent:', data);
        setMessageToTutor('');
      })
      .catch(error => console.error('Error sending message:', error));
  };

  const renderStarRating = () => {
    const stars = [];
    const maxRating = 5;

    for (let i = 1; i <= maxRating; i++) {
      const starClass = i <= rating ? 'star-filled' : 'star-unfilled';

      stars.push(
        <span
          key={i}
          className={starClass}
          onClick={() => setRating(i)}
        >
          &#9733;
        </span>
      );
    }

    return stars;
  };

  return (
    <div>
      <h1>Tutor's Public Profile</h1>
      <img
        src={
          profileAddress === ''
            ? require('../Storage/default')
            : require('../Storage/' + email)
        }
        style={{ width: 120, height: 140 }}
        alt="Profile"
      />
      <p>First Name: {firstName}</p>
      <p>Last Name: {lastName}</p>
      <p>Biography: {biography}</p>
      <p>Profile Address: {profileAddress}</p>
      <br />
      <h1>Courses:</h1>
      {courses.length > 0 ? (
        <ul>
          {courses.map((course, index) => (
            <li key={index}>
              Subject: {course['subject']}; Lesson price: {course['price']};
            </li>
          ))}
        </ul>
      ) : (
        <p>No courses available</p>
      )}
      <h1>Reviews</h1>
      {reviews.length > 0 ? (
        <ul>
          {reviews.map((review, index) => (
            <li key={index}>
              Review: {review && review['review_text']}; Reviewer: {review && review['student_mail']};
            </li>
          ))}
        </ul>
      ) : (
        <p>No reviews</p>
      )}
      <div>
        <h1>Rate the Tutor:</h1>
        {renderStarRating()}
      </div>
      {is_tutor_student && (
        <div>
          <h1>Add a Review</h1>
          <input
            type="text"
            value={reviewText}
            onChange={event => setReviewText(event.target.value)}
          />
          <button onClick={handleReviewAddition}>Add Review</button>
        </div>
      )}
      <div>
        <h1>Send a Message to the Tutor</h1>
        <input
          type="text"
          value={messageToTutor}
          onChange={event => setMessageToTutor(event.target.value)}
        />
        <button onClick={handleSendMessage}>Send Message</button>
      </div>
    </div>
  );
};

export default PublicTutor;
