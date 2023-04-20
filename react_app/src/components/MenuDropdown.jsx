import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import React from "react"
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { logout, getAuth } from '../components/postService'

const MenuDropdown = () => {
    const user = getAuth()
    const navigate = useNavigate();
    
    return (
        <div>
            {
                user ?
                    
                <DropdownButton id = "dropdown-basic-button" title = "Меню">    
                        <Dropdown.Item>
                            <Link to="user/" className="nav-link">Личный кабинет</Link>
                        </Dropdown.Item >

                        <Dropdown.Item>
                            <Link to="new/" className="nav-link">Добавить идею</Link> 
                        </Dropdown.Item>

                        <Dropdown.Item>
                            <Link to="new_rubric/" className="nav-link">Добавить рубрику</Link>
                        </Dropdown.Item>
                    
                            {
                                user.is_superuser ?
                                <Dropdown.Item>
                                    <Link to="adminview/" className="nav-link">Страница администратора</Link>
                                </Dropdown.Item>
                                :
                                <br />
                            }
                        <Dropdown.Item>
                            <a className="nav-link" onClick={logout} href="/" tabIndex="-1" aria-disabled="true">Выход</a>
                        </Dropdown.Item>
                </DropdownButton>
                :

                <DropdownButton id = "dropdown-basic-button" title = "Меню"> 
                    <Dropdown.Item>
                        <Link to="login/" className="nav-link">Войти</Link>
                    </Dropdown.Item>
                    <Dropdown.Item>
                        <Link to="register/" className="nav-link">Регистрация</Link>
                    </Dropdown.Item>
                </DropdownButton>
            }
        </div>
        
// {
//     user ?
//         <div>
//             <li className="nav-item">
//                 <Link to="user/" className="nav-link">Личный кабинет</Link>
//             </li>
//             <li className="nav-item">
//                 <Link to="new/" className="nav-link">Добавить идею</Link>
//             </li>
//             <li className="nav-item">
//                 <Link to="new_rubric/" className="nav-link">Добавить рубрику</Link>
//             </li>
//             {
//                 user.is_superuser ?
//                     <li className="nav-item">
//                         <Link to="adminview/" className="nav-link">Страница администратора</Link>
//                     </li>
//                     :
//                     <br />
//             }
//             <li className="nav-item">
//                 <a className="nav-link" onClick={logout} href="/" tabIndex="-1" aria-disabled="true">Выход</a>
//             </li>

//         </div>

//         :
//         <div>
//             <li className="nav-item">
//                 <Link to="login/" className="nav-link">Войти</Link>
//                 {/* <Button text="Войти в систему" type="button" styles="mainButton" action={togleVisable}/> */}
//             </li>

//         </div>
// }
  );
}

export default MenuDropdown;