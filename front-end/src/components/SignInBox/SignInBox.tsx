import { Link } from "react-router-dom";
import "./SignInBox.css";
import { useState, useEffect, FormEvent } from "react";
interface SignInBoxProps {
  close: () => void;
  boxVisibility: boolean;
}

export default function SignInBox(props: SignInBoxProps) {
  const [containerVisibility, setContainerVisibility] = useState(false);
  const [signInBoxVisibility, setSignInBoxVisibility] = useState(false);
  useEffect(() => {
    if (props.boxVisibility) {
      setContainerVisibility(true);
      setTimeout(() => {
        setSignInBoxVisibility(true);
      }, 30);
    } else {
      setSignInBoxVisibility(false);
      setTimeout(() => {
        setContainerVisibility(false);
      }, 300);
    }
  }, [props.boxVisibility]);
  const submitAction = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
  };

  return (
    <div
      className={`sign-in-container ${
        containerVisibility
          ? "sign-in-container-visible"
          : "sign-in-container-hidden"
      }`}
    >
      <div
        className={`sign-in-box ${
          signInBoxVisibility ? "open-sign-in-box" : "close-sign-in-box"
        }`}
      >
        <button className="sign-in-close-btn" onClick={props.close}>X</button>
        <h1 className="sign-in-title">Sign In</h1>
        <form className="sign-in-form" onSubmit={submitAction}>
          <label className="sign-in-elements sign-in-label" htmlFor="username">
            Username
          </label>
          <input
            className="sign-in-elements sign-in-input"
            type="text"
            id="username"
            name="username"
          />
          <label className="sign-in-elements sign-in-label" htmlFor="password">
            Password
          </label>
          <input
            className="sign-in-elements sign-in-input"
            type="password"
            id="password"
            name="password"
          />
          <div className="sing-in-btn-container sign-in-box-btn-container">
            <button className="sign-in-box-btn sign-in-elements" type="submit">
              Sign In
            </button>
            <Link to="/singup" className="sign-in-elements">
              don't have an account?
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
}
