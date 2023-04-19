import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import React, { useEffect, useState } from "react";
import { getAllUsers } from './postService'
import UserItem from "./UserItem";

const AdminMenu = () => {

    const [usersList, setUsers] = useState([])

    useEffect(() => {
        getAllUsers()
            .then(res => { setUsers(res.data.results) })
            .catch((error) => alert.error(error.message))

    }, [setUsers]);
    console.log('users\n', usersList)

    return (

        <Tabs
            defaultActiveKey="profile"
            id="uncontrolled-tab-example"
            className="mb-3"
        >
            <Tab eventKey="home" title="Пользователи">
                <div class="container-fluid">
                    <div class="row justify-content-center align-items-center g-2">
                        <div class="col-1"> </div>
                        <div class="col">Логин</div>
                        <div class="col">Емаил</div>
                        <div class="col">Статус</div>
                        <div class="col">Изменить статус</div>
                    </div>
                </div>
                <ol>
                    {usersList.map(userItem =>

                        <li>
                            <UserItem userItem={userItem} key={userItem.id} />
                        </li>
                    )}

                </ol>
            </Tab>
            <Tab eventKey="posts" title="Посты">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, pariatur suscipit quibusdam, mollitia distinctio ea qui facilis vitae perspiciatis, accusantium necessitatibus commodi sint ad. Natus molestias nulla soluta eligendi tempore?</p>
            </Tab>
        </Tabs>
    );
}

export default AdminMenu;