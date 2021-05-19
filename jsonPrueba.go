package main

import (
	"encoding/json"
	// "io/ioutil"
	"fmt"
	"log"
	"net/http"
)

func main() {

	var data map[string]interface{}

	resp, err := http.Get("https://v2.jokeapi.dev/joke/Programming?amount=3")
	if err != nil {
		log.Fatalln(err)
	}
	json.NewDecoder(resp.Body).Decode(&data)

	// bromas = data["jokes"]
	// fmt.Println(bromas)
	// defer resp.Body.Close()
	//We Read the response body on the line below.
	// body, err := ioutil.ReadAll(resp.Body)
	// if err != nil {
	// 	log.Fatalln(err)
	// }
	//Convert the body to type string
	// sb := string(body)
	// log.Printf(bodyData)
	fmt.Println(data["amount"])

}
