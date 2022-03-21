import React, { Component } from "react";
import styled, { css } from "styled-components";

function ReportScreen(props) {
  return (
    <>
      <LogoStack>
        <Logo
          src={require("../assets/images/Screen_Shot_2022-03-18_at_2.09.45_PM2.png")}
        ></Logo>
        <Camara></Camara>
        <Header></Header>
      </LogoStack>
      <TomarFotoRow>
        <TomarFoto>
          <ButtonOverlay></ButtonOverlay>
        </TomarFoto>
        <RepetirFoto>
          <ButtonOverlay></ButtonOverlay>
        </RepetirFoto>
      </TomarFotoRow>
      <EnviarFoto>
        <ButtonOverlay></ButtonOverlay>
      </EnviarFoto>
      <Historial>
        <ButtonOverlay></ButtonOverlay>
      </Historial>
    </>
  );
}

const Logo = styled.img`
  top: 50px;
  width: 254px;
  height: 230px;
  position: absolute;
  left: 61px;
  object-fit: contain;
`;

const ButtonOverlay = styled.button`
 display: block;
 background: none;
 height: 100%;
 width: 100%;
 border:none
 `;
const Camara = styled.div`
  top: 241px;
  left: 47px;
  width: 281px;
  height: 256px;
  position: absolute;
  background-color: #E6E6E6;
`;

const Header = styled.div`
  top: 0px;
  left: 0px;
  width: 392px;
  height: 90px;
  position: absolute;
  background-color: rgba(204,204,36,1);
`;

const LogoStack = styled.div`
  width: 392px;
  height: 498px;
  margin-top: -34px;
  position: relative;
`;

const TomarFoto = styled.div`
  width: 122px;
  height: 92px;
  background-color: #E6E6E6;
  border: none;
`;

const RepetirFoto = styled.div`
  width: 122px;
  height: 92px;
  background-color: #E6E6E6;
  margin-left: 37px;
  border: none;
`;

const TomarFotoRow = styled.div`
  height: 92px;
  flex-direction: row;
  display: flex;
  margin-top: 39px;
  margin-left: 47px;
  margin-right: 47px;
`;

const EnviarFoto = styled.div`
  width: 281px;
  height: 65px;
  background-color: #E6E6E6;
  margin-top: 22px;
  margin-left: 47px;
  border: none;
`;

const Historial = styled.div`
  width: 281px;
  height: 69px;
  background-color: #E6E6E6;
  margin-top: 20px;
  margin-left: 47px;
  border: none;
`;

export default ReportScreen;
