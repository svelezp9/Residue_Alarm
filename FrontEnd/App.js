import React, { useState } from "react";
import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import { createDrawerNavigator } from "react-navigation-drawer";
import AppLoading from "expo-app-loading";

import * as Font from "expo-font";
import InicioScreen from "./src/screens/InicioScreen";
import InicioSesion from "./src/screens/InicioSesion";
import ReportScreen from "./src/screens/ReportScreen";

const DrawerNavigation = createDrawerNavigator({
  InicioScreen: InicioScreen,
  InicioSesion: InicioSesion,
  ReportScreen: ReportScreen
});

const StackNavigation = createStackNavigator(
  {
    DrawerNavigation: {
      screen: DrawerNavigation
    },
    InicioScreen: InicioScreen,
    InicioSesion: InicioSesion,
    ReportScreen: ReportScreen
  },
  {
    headerMode: "none"
  }
);

const AppContainer = createAppContainer(StackNavigation);

function App() {
  const [isLoadingComplete, setLoadingComplete] = useState(false);
  if (!isLoadingComplete) {
    return (
      <AppLoading
        startAsync={loadResourcesAsync}
        onError={handleLoadingError}
        onFinish={() => handleFinishLoading(setLoadingComplete)}
      />
    );
  } else {
    return isLoadingComplete ? <AppContainer /> : <AppLoading />;
  }
}
async function loadResourcesAsync() {
  await Promise.all([
    Font.loadAsync({
      "roboto-regular": require("./src/assets/fonts/roboto-regular.ttf")
    })
  ]);
}
function handleLoadingError(error) {
  console.warn(error);
}

function handleFinishLoading(setLoadingComplete) {
  setLoadingComplete(true);
}

export default App;
