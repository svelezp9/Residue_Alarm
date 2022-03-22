import React, { Component } from "react";
import { StyleSheet, View, Image, TouchableOpacity } from "react-native";

function ReportScreen(props) {
  return (
    <View style={styles.container}>
      <View style={styles.logoStack}>
        <Image
          source={require("../assets/images/Screen_Shot_2022-03-18_at_2.09.45_PM2.png")}
          resizeMode="contain"
          style={styles.logo}
        ></Image>
        <View style={styles.camara}></View>
        <View style={styles.header}></View>
      </View>
      <View style={styles.tomarFotoRow}>
        <TouchableOpacity style={styles.tomarFoto}></TouchableOpacity>
        <TouchableOpacity style={styles.repetirFoto}></TouchableOpacity>
      </View>
      <TouchableOpacity style={styles.enviarFoto}></TouchableOpacity>
      <TouchableOpacity style={styles.historial}></TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1
  },
  logo: {
    top: 50,
    width: 254,
    height: 230,
    position: "absolute",
    left: 61
  },
  camara: {
    top: 241,
    left: 47,
    width: 281,
    height: 256,
    position: "absolute",
    backgroundColor: "#E6E6E6"
  },
  header: {
    top: 0,
    left: 0,
    width: 392,
    height: 90,
    position: "absolute",
    backgroundColor: "rgba(204,204,36,1)"
  },
  logoStack: {
    width: 392,
    height: 498,
    marginTop: -34
  },
  tomarFoto: {
    width: 122,
    height: 92,
    backgroundColor: "#E6E6E6"
  },
  repetirFoto: {
    width: 122,
    height: 92,
    backgroundColor: "#E6E6E6",
    marginLeft: 37
  },
  tomarFotoRow: {
    height: 92,
    flexDirection: "row",
    marginTop: 39,
    marginLeft: 47,
    marginRight: 47
  },
  enviarFoto: {
    width: 281,
    height: 65,
    backgroundColor: "#E6E6E6",
    marginTop: 22,
    marginLeft: 47
  },
  historial: {
    width: 281,
    height: 69,
    backgroundColor: "#E6E6E6",
    marginTop: 20,
    marginLeft: 47
  }
});

export default ReportScreen;
