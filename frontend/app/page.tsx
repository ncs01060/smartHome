"use client";
import { useState } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";

axios.defaults.withCredentials = true;

export default function Home() {
  const router = useRouter();
  const [name, setName] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const loginButtonClick = () => {
    if (name == "" || password == "") {
      alert("이름 혹은 비밀번호를 입력해주세요!");
      return;
    }

    axios
      .post(`${process.env.NEXT_PUBLIC_SERVER_URL}/auth/login`, {
        username: name,
        password: password,
      })
      .then(function (response) {
        router.push("/Dashboard");
      })
      .catch(function (error) {
        console.error(error);
      });
  };

  return (
    <div className="border">
      <div className="LoginForm">
        <h3>로그인</h3>
        <p>
          <input
            type="text"
            placeholder="유저 이름"
            value={name}
            onChange={(e) => {
              setName(e.target.value);
            }}
          />
        </p>
        <p>
          <input
            type="password"
            placeholder="비밀번호"
            value={password}
            onChange={(e) => [setPassword(e.target.value)]}
          />
        </p>
        <button onClick={loginButtonClick}>로그인</button>
      </div>
    </div>
  );
}
