import './styles/bootstrap.min.css';
import './styles/styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import {createBrowserRouter, RouterProvider,} from "react-router-dom";
import useModal from './services/castomHooks/useModal';

import Lk from './components/Lk';
import ErrorPage from './components/ErrorPage';
import Registration from './components/Make/Registration';
import LogIn from './components/LogIn';
import MakeRubric from './components/Make/MakeRubric';
import MakeIdea from  './components/Make/MakeIdea'
import OneIdea from './components/OneIdea'
import Main from './components/Main';
import Title from './components/Title'
import Welcome from './components/Welcome';

function App() {
  const [isVisable, togleVisable] = useModal()






  const router = createBrowserRouter([
    {
      path: "/",
      element: <Title isVisable={isVisable} togleVisable={togleVisable}/>,
      errorElement: <ErrorPage />,
      basename: '/',
      children: [
        {
          path: "/",
          element: <Main />,
        },
        {
          path: "user/",
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
          element: <MakeIdea />,
        },
        {
          path: "new_rubric/",
          element: <MakeRubric />,
        },
        {
          path: "idea/",
          element: <OneIdea />,
        },
        {
          path: "welcome/",
          element: <Welcome />,
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
