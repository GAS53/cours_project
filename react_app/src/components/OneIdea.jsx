import React, { useEffect, useState } from "react"
import { useSearchParams } from "react-router-dom";
import { Link } from "react-router-dom";
import { getAuth, getIdea, connectToIdea, LikeIdea } from "./postService";
import { useNavigate } from "react-router-dom";



function OneIdea() {
    const navigate = useNavigate();
    const [queryParameters] = useSearchParams()
    const idea_id = queryParameters.get('id')
    console.log('idea_id')
    console.log(idea_id)
    const [ myId, setMyId ] = useState()
    const [oneIdea, setOneIdea] = useState([])





    useEffect(() => {
        const auth = getAuth()
        console.log('auth')
        console.log(auth)
        setMyId(auth.id)
        if (auth) {
            getIdea(idea_id)
                .then(res =>  { setOneIdea(res.data) })
                .catch(res => {alert(res)})
        } else { navigate( '/welcome/') }
        },[oneIdea])


    function connectHandler(e) {
        connectToIdea(idea_id)
            .then(res => {
                    alert(`вы вступили в команду ${oneIdea.title}`)
                })
            .catch((error) => {
                if (error.response.status === 423 ) {
                        alert(`вы вышли из команды ${oneIdea.title}`)
                    } else {
                    alert(`ошибка при добавлении пользователя  ${error.message}`)}})
    }

    function likeHandler(e) {
        const auth = getAuth()
        if (oneIdea.likesToIdea.indexOf(auth.id) === -1) {
            const data = {
                idea: idea_id,
                autor: auth.id
            }
            LikeIdea(data)
                .then(alert(`вы ${auth.login} лайкнули ${oneIdea.title}`))
                .catch((error) => {
                    if (error.response.status === 423 ) {
                        alert(`вы убрали лайк ${oneIdea.title}`)
                    } else {
                        alert(`ошибка при добавлении лайка ${error.message}`)}})
    }}

    if (oneIdea.joinedUser===undefined) {
        return (<dvi><h3>Страница загружается</h3></dvi>)
    } else {

    return (
        <div className="card mb-3" style={{minHeight: '166px', minWidth: '380px'}}>
                        <div className="card-body">

                            <div className="row g-3 justify-content-left">

                                <div className="col-sm-2 card-image d-none d-md-block my-auto">
                                    
                                </div>

                                <div className="col" style={{minWidth: '340px'}}>

                                    <div className="container">
                                        <div className="row justify-content-center align-items-center g-2">
                                            <div className="col-4">
                                                <h4 className="card-title text-center">
                                                    <strong>{oneIdea.title}</strong>

                                                </h4>
                                            </div>
                                        </div>

                                        <div className="row g-1">

                                            <div className="col-4 my-auto">
                                                <Link className="nameLink" to='/' >idea</Link>
                                            </div>



                                            <div className="col-1 my-auto">
                                                <small className="text-muted">(1)</small>
                                            </div>
                                        
                                            <div className="row justify-content-center align-items-center g-2">
                                                <div className="col">
                                                    <p className="card-text">Описание</p>
                                                    <p>{oneIdea.body}</p>
                                                    <p className="card-text">
                                                        <small className="text-muted">Опубликовано {oneIdea.created}
                                                            года</small>
                                                    </p>
                                                </div>
                                            </div>

                                        </div>
                                    </div>

                                </div>

                                <div className="col-3 my-auto">
                                    <div className="container">
                                        <div className="row g-2 mx-auto justify-content-center">

                                            <div className="col">
                                                <div className="mt-2 text-center text-muted">
                                                    <strong>{oneIdea.rubric.rubirc_name}</strong>
                                                </div>
                                                <div className="mt-2 text-center">
                                                    <h1>⭐⭐⭐⭐⭐</h1>
                                                </div>
                                                
                                                    <div className="mt-2 d-grid gap-2">
                                                        <button type="button" onClick={connectHandler} className="btn mainButton">
                                                        { oneIdea.joinedUser.indexOf(myId) ?  <p>Выйти из команды</p>  : <p>Вступить в команду</p>  }
                                                        </button>
                                                    </div>
                                                <div className="mt-2 d-grid gap-2">
                                                    <button type="button" onClick={likeHandler} className="btn btn-outline-warning">
                                                        Лайкнуть
                                                    </button>
                                                </div>

                                        </div>
                                    </div>
                                </div>

                            </div>


                            <div className="row justify-content-center align-items-center g-2">
                                <div className="col">
                                    <div>
                                        { oneIdea.joinedUser === undefined ?
                                        `Ты можешь первым присоедениться в команду`
                                            :
                                        `Уже с нами ${oneIdea.joinedUser.length} человек`}
                                    </div>
                                    <div>
                                        { oneIdea.likesToIdea === undefined ?
                                        `` : `Идея набрала ${oneIdea.likesToIdea.length} лайков`}
                                    </div>   

                                </div>
                        </div>
                    </div>
                </div>
            </div>

                         
        ) 
}}

export default OneIdea;