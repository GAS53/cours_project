import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
  const error = useRouteError();
  console.error(error);

  return (
    <div>
      <div className="container-md mt-5 idea-list">
        <div className="row justify-content-center align-items-top">
          <h1>Ой-ой</h1>
          <p>Что-то пошло не так</p>
          <h3>Запрашиваемой страници не существует</h3>
          <p>
            <i>{error.statusText || error.message}</i>
          </p>
        </div>
      </div>
    </div>
  );
}
