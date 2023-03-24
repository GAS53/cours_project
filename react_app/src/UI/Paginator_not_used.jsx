import React from "react"

function Title() {

    return (
        <nav aria-label="Page navigation example">
        <ul className="pagination justify-content-end">
            <li className="page-item disabled">
                <a className="page-link" href="#" tabindex="-1" aria-disabled="true">Назад</a>
            </li>
            <li className="page-item"><a className="page-link active" href="#">1</a></li>
            <li className="page-item"><a className="page-link" href="#">2</a></li>
            <li className="page-item"><a className="page-link" href="#">3</a></li>
            <li className="page-item">
                <a className="page-link" href="#">Далее</a>
            </li>
        </ul>
    </nav>
        )
    }

export default Title