import React, { Component } from "react";
import styled, { css } from "styled-components";
import CrearCuenta from "../components/CrearCuenta";

function InicioScreen(props) {
  return (
    <>
      <HeaderPhoneRow>
        <HeaderPhone></HeaderPhone>
        <Rect3></Rect3>
      </HeaderPhoneRow>
      <Logo
        src={require("../assets/images/Screen_Shot_2022-03-18_at_2.09.45_PM.png")}
      ></Logo>
      <BotonEmail>
        <ButtonOverlay>
          <Email>Email</Email>
        </ButtonOverlay>
      </BotonEmail>
      <BotonPasswordStack>
        <BotonPassword>
          <ButtonOverlay></ButtonOverlay>
        </BotonPassword>
        <Password>Password</Password>
      </BotonPasswordStack>
      <BotonCrearCuenta>
        <CrearCuenta
          style={{
            height: 28,
            width: 89,
            marginLeft: 147
          }}
        ></CrearCuenta>
      </BotonCrearCuenta>
    </>
  );
}

const HeaderPhone = styled.div`
  width: 392px;
  height: 90px;
  background-color: rgba(204,204,36,1);
`;

const ButtonOverlay = styled.button`
 display: block;
 background: none;
 height: 100%;
 width: 100%;
 border:none
 `;
const Rect3 = styled.div`
  width: 392px;
  height: 90px;
  background-color: rgba(204,204,36,1);
  margin-left: 24px;
`;

const HeaderPhoneRow = styled.div`
  height: 90px;
  flex-direction: row;
  display: flex;
  margin-top: -34px;
  margin-right: -433px;
`;

const Logo = styled.img`
  width: 290px;
  height: 301px;
  margin-top: 12px;
  margin-left: 46px;
  object-fit: contain;
`;

const BotonEmail = styled.div`
  width: 298px;
  height: 68px;
  background-color: #E6E6E6;
  flex-direction: column;
  display: flex;
  margin-top: 37px;
  margin-left: 38px;
  border: none;
`;

const Email = styled.span`
  font-family: Roboto;
  font-style: normal;
  font-weight: 400;
  color: #121212;
  margin-top: 52px;
  margin-left: 262px;
`;

const BotonPassword = styled.div`
  top: 0px;
  left: 0px;
  width: 298px;
  height: 68px;
  position: absolute;
  background-color: #E6E6E6;
  border: none;
`;

const Password = styled.span`
  font-family: Roboto;
  top: 53px;
  left: 232px;
  position: absolute;
  font-style: normal;
  font-weight: 400;
  color: #121212;
`;

const BotonPasswordStack = styled.div`
  width: 298px;
  height: 69px;
  margin-top: 49px;
  margin-left: 42px;
  position: relative;
`;

const BotonCrearCuenta = styled.div`
  width: 384px;
  height: 45px;
  background-color: rgba(204,204,35,1);
  flex-direction: column;
  display: flex;
  margin-top: 175px;
  margin-left: 4px;
`;

export default InicioScreen;
