import { useState } from 'react';

export const useToken = () => {
  const getToken = () => {
    const userToken = JSON.parse(sessionStorage.getItem('token'));
    return userToken === null? '' : userToken;
  };

  const [token, setToken] = useState(getToken());

  const updateToken = userToken => {
    sessionStorage.setItem('token', JSON.stringify(userToken));
    setToken(userToken);
  };

  return {
    token,
    setToken: updateToken,
  };
}
