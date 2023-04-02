import './styles/bootstrap.min.css';
import './styles/styles.css';

import Main from './components/Main';
import Title from './components/Title'
// import Body from './UI/Body';
import Lk from './components/Lk';
import ErrorPage from './components/ErrorPage';
import Registration from './components/Registration';
import LogIn from './components/LogIn';
// import ProtectedRoute from './API/ProtectedRoute';
import NewIdea from './components/NewIdea';
import React, {useEffect, useState} from 'react';
import useUserActions from "../src/API/useUserActions";


import {createBrowserRouter, RouterProvider,} from "react-router-dom";
import useModal from './services/castomHooks/useModal';

function App() {
  const [isVisable, togleVisable] = useModal()






  const router = createBrowserRouter([
    {
      path: "/",
      element: <Title isVisable={isVisable} togleVisable={togleVisable}/>,
      // errorElement: <ErrorPage />, // временно для тестирования
      children: [
        {
          path: "/",
          element: <Main />,
        },
        {
          path: "lk/",
          element: <Lk />,
        },
        {
          path: "register/",
          element: <Registration />,
        },
        {
          path: "login/",
          element: <LogIn />,
        },
        {
          path: "new/",
          element: <NewIdea />,
        },
      ]
    },
  ]);

  return (
    <div>
      {/* <ProtectedRoute> */} 
        <RouterProvider router={router} /> 
      {/* </ProtectedRoute> */}
    </div>
  );
}

export default App;
