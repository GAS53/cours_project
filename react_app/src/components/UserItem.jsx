import React from "react";
import { togleStatus } from "./postService";

const UserItem = ({ userItem }) => {

    console.log(togleStatus)

    function togleHandler(e) {
        togleStatus(userItem.id, userItem.is_active)
            .then(res => {
                alert(`Статус пользователя изменен ${userItem.login}`)
            })
            .catch((error) => {
                alert(`Ошибка изменения статуса  ${error.message}`)
            })
    }

    return (

        <div class="container mb-2">

            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <div class="row justify-content-center align-items-center g-2">

                                <div class="col">{userItem.login}</div>
                                <div class="col">{userItem.email}</div>
                                <div class="col">{userItem.is_active ? "✅" : '❌'}</div>
                                <div class="col">
                                    {userItem.is_active ?
                                        <button type="button" onClick={togleHandler} className="btn btn-outline-danger">
                                            Заблокировать
                                        </button>
                                        :
                                        <button type="button" onClick={togleHandler} className="btn btn-outline-success">
                                            Разблокировать
                                        </button>
                                    }

                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )
}

export default UserItem