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


import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import useModal from './services/castomHooks/useModal';

function App() {
  const [isVisable, togleVisable] = useModal()
  const user = (
    {
      id: 1,
      age: 18,
      nickname: "UralFox",
      email: "admin@zadolbal.net",
      username: "Илья",
      surname: "Куликов",
      avatar: "https://img.freepik.com/free-vector/mysterious-mafia-man-smoking-cigarette_52683-34828.jpg?w=826&t=st=1678618018~exp=1678618618~hmac=ea416d598467ae43cc431081515e0bb0a25e41cb22385a045ec12ca347842f9a",
      password: "qwe123",
      registrationdate: "35.15.3984",
      is_active: true,
      is_superuser: false,
    }
  );

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
          element: <Lk user={user} />,
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
