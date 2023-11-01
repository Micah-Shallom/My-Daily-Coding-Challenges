package challenges

import (
	"encoding/json"
	"fmt"
	"log"
)

type Person struct {
	Name string `json:"customName"`
	Age int `json:"age"`
	CreditCard string `json:"-"`
}

func jsonsolution() {

}

func ManipulatingJSON() {
	p := Person{Name: "Shallom", CreditCard: "super secret"}
	pBytes, err := json.Marshal(p)
	log.Print(string(pBytes))
	fmt.Println( err)


	p2AsRawJson := json.RawMessage(`{"CustomName":"Faith"}`)
	var p2 Person
	err2 := json.Unmarshal(p2AsRawJson, &p2) 
	log.Print(err2)
	log.Printf("%+v", p2)

}