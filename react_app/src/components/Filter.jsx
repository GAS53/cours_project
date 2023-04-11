import React, { useEffect, useState } from "react"
import { Button } from "./UI/button/Button";
import Rudiobutton from "./Rudiobutton"

function Filter(props) {

    const [filreres, setFilteres] = useState([])

    useEffect(() => {
        let arr = props.val.reduce((result, item) => {
            return result.includes(item) ? result : [... result, item];}, []);
        console.log(arr)
        setFilteres(arr)
    
    }, [setFilteres])

        
    return (
        
        <div className="col-md-3 d-none d-md-block">
            <h3>Фильтр</h3>
            {/* <form className="row g-3">
                <div className="col">
                    {filreres.map(fl => (<Rudiobutton value={fl}/>))}
                    <Button text="Фильтровать" type="submit" styles="mainButton"/>
                </div>
            </form> */}

        </div>
        )
    
}
export default Filter;