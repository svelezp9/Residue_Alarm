import React, { Component } from "react";
import { StyleSheet, View, Image, TouchableOpacity, Text } from "react-native";
import CrearCuenta from "../components/CrearCuenta";

function InicioSesion(props) {
  return (
    <View style={styles.container}>
      <View style={styles.headerPhoneRow}>
        <View style={styles.headerPhone}></View>
        <View style={styles.rect3}></View>
      </View>
      <Image
        source={require("../assets/images/Screen_Shot_2022-03-18_at_2.09.45_PM.png")}
        resizeMode="contain"
        style={styles.logo}
      ></Image>
      <View style={styles.botonEmailStack}>
        <TouchableOpacity style={styles.botonEmail}></TouchableOpacity>
        <Text style={styles.email}>Email</Text>
      </View>
      <View style={styles.botonPasswordStack}>
        <TouchableOpacity style={styles.botonPassword}></TouchableOpacity>
        <Text style={styles.password}>Password</Text>
      </View>
      <View style={styles.botonCrearCuenta}>
        <CrearCuenta style={styles.crearCuenta}></CrearCuenta>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  headerPhone: {
    width: 392,
    height: 90,
    backgroundColor: "rgba(204,204,36,1)"
  },
  rect3: {
    width: 392,
    height: 90,
    backgroundColor: "rgba(204,204,36,1)",
    marginLeft: 24
  },
  headerPhoneRow: {
    height: 90,
    flexDirection: "row",
    marginTop: -34,
    marginRight: -433
  },
  logo: {
    width: 290,
    height: 301,
    marginTop: 12,
    marginLeft: 46
  },
  botonEmail: {
    top: 0,
    left: 0,
    width: 298,
    height: 68,
    position: "absolute",
    backgroundColor: "#E6E6E6"
  },
  email: {
    top: 52,
    left: 262,
    position: "absolute",
    fontFamily: "roboto-regular",
    color: "#121212"
  },
  botonEmailStack: {
    width: 298,
    height: 69,
    marginTop: 37,
    marginLeft: 38
  },
  botonPassword: {
    top: 0,
    left: 0,
    width: 298,
    height: 68,
    position: "absolute",
    backgroundColor: "#E6E6E6"
  },
  password: {
    top: 53,
    left: 232,
    position: "absolute",
    fontFamily: "roboto-regular",
    color: "#121212"
  },
  botonPasswordStack: {
    width: 298,
    height: 70,
    marginTop: 48,
    marginLeft: 42
  },
  botonCrearCuenta: {
    width: 384,
    height: 45,
    backgroundColor: "rgba(204,204,35,1)",
    marginTop: 174,
    marginLeft: 4
  },
  crearCuenta: {
    height: 28,
    width: 89,
    marginLeft: 147
  }
});

export default InicioSesion;
