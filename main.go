package main

import (
	"io/ioutil"
	"log"
	"net/http"
)

// imports for http requests

// datos importantes
// html_url : este es el url que abre el issue para verlo en github
// title : Nombre del Issue
// number: Numero del Issue
// user[login] : Nombre del Autor del Issue
// labels: Lista de Tags
// milestone[title] : Nombre del Milestone
// milestone[description] : Descripcion del Milestone

func main() {
	resp, err := http.Get("https://api.github.com/repos/golang/go/issues?labels=Go2")
	if err != nil {
		log.Fatalln(err)
	}
	// defer resp.Body.Close()
	//We Read the response body on the line below.
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	//Convert the body to type string
	sb := string(body)
	log.Printf(sb)
}
