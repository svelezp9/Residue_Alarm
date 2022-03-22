import React, { Component } from "react";
import { StyleSheet, View, Text } from "react-native";

function CrearCuenta(props) {
  return (
    <View style={[styles.container, props.style]}>
      <Text style={styles.text}>Crear Cuenta</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {},
  text: {
    fontFamily: "roboto-regular",
    color: "#121212",
    height: 28,
    width: 89
  }
});

export default CrearCuenta;
