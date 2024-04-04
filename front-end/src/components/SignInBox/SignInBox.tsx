import "./SignInBox.css";

interface SignInBoxProps {
  close: () => void;
  boxVisibility: boolean;
}

export default function SignInBox(props: SignInBoxProps) {
  return (
      <div
        className={`SignInBox ${
          props.boxVisibility ? "open-sign-in-box" : "close-sign-in-box"
        }`}
      >
        <h1>Sign In</h1>
        <form className="sign-in-form ">
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
          <button className="sign-in-box-btn sign-in-elements">Sign In</button>
          <button
            className={`sign-in-box-btn sign-in-elements`}
            onClick={props.close}
          >
            Close
          </button>
        </form>
      </div>
  );
}
