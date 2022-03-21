import React, { Component } from "react";
import styled, { css } from "styled-components";

function CrearCuenta(props) {
  return (
    <Container {...props}>
      <Text>Crear Cuenta</Text>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  flex-direction: column;
`;

const Text = styled.span`
  font-family: Roboto;
  font-style: normal;
  font-weight: 400;
  color: #121212;
  height: 28px;
  width: 89px;
`;

export default CrearCuenta;
