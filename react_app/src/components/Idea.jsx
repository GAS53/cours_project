import React from "react";

const Idea = (props) => { 

    return (

        <div className="card mb-3" style={{minWidth: '380px', minHeight: '166px'}}>
            <div className="card-body">
                <div className="row g-3 justify-content-left">

                    <div className="col-sm-2 card-image d-none d-md-block my-auto">Card title</div>

                                <div className="col" style={{minWidth: "340px"}}>

                                    <div className="container">
                                        <div className="row justify-content-center align-items-center g-2">
                                            <h4 className="card-title text-center"><strong>{props.title}</strong></h4>
                                        </div>

                                        <div className="row g-1">

                                            <div className="col-4 my-auto">
                                                <a className="nameLink" href="#">{props.created_at}</a>
                                            </div>

                                            <div className="col my-auto">
                                                <div className="progress">
                                                    <div className="progress-bar progress-bar-striped" role="progressbar"
                                                        style={{width: '10%', ariaValuenow: '10', ariaValuemin: '0'}}  
                                                        aria-valuemax="100"></div>
                                                </div>
                                            </div>

                                            <div className="col-1 my-auto">
                                                <small className="text-muted">(1)</small>
                                            </div>
                                            <div className="row justify-content-center align-items-center g-2">
                                                <div className="col">
                                                    <p className="card-text">Описание</p>
                                                    <p>{props.preview}</p>
                                                    <p className="card-text">
                                                        <small className="text-muted">Опубликовано: {props.created_at}</small>
                                                    </p>
                                                </div>
                                            </div>

                                        </div>
                                    </div>
                                </div>

                                <div className="col-1 my-auto">
                                    <div className="container">
                                        <div className="row g-2 mx-auto justify-content-center">

                                            <div className="col">
                                                <div className="serviceButton">
                                                    <a className="nav-link " href="#"></a>
                                                </div>
                                            </div>

                                            <div className="col">
                                                <div className="serviceButton">
                                                    <a className="nav-link " href="#"></a>
                                                </div>
                                            </div>

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

    )
}

export default Idea
