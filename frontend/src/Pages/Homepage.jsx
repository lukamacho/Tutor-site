import backgroundImage from '../Images/HomepageBG.png';

export const background = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
};

export default function Homepage() {
  const inspiringSentenceStyle = {
    fontSize: '48px',
    fontWeight: 'bold',
    color: '#ff0000',
    textAlign: 'center',
    paddingTop: '40vh',
    textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)',
  };

  return (
    <div style={background}>
      <h1 style={inspiringSentenceStyle}>Your Olympic carrier starts here</h1>
    </div>
  );
}
