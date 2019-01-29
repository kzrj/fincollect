import React, { Component } from 'react';

class App extends Component {
  constructor(props){
        super(props);
        this.state = {
            currencies: [
              {shortName: "USD", value: 1},
              {shortName: "EUR", value: 2},
              {shortName: "PLN", value: 3},
              {shortName: "CZK", value: 4},
            ],
            fromCurrency: 1,
            toCurrency: 1,
            amount: 0,
            totalAmount: 0,
            rate: 0,

        };
        this.handleChange = this.handleChange.bind(this);
        this.getRate = this.getRate.bind(this);
    }

  handleChange(event) {
    const target = event.target;
    const name = target.name;

    this.setState({
      [name]: target.value
    });
  }

  getRate(){
    var url = new URL("http://localhost:8000/api/rate/"),
    params = {
      master_currency:this.state.fromCurrency,
      slave_currency:this.state.toCurrency,
      amount: this.state.amount
    }
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
    
    fetch(url)
      .then((response) => 
      {
        return response.json()
      })
      .then((data) =>{
        this.setState({
          rate: data.rate
        })
        this.setState({
          totalAmount: data.total_amount
        })
      })
      

  }

  render() {
    let total = this.state.totalAmount
    let rate = this.state.rate

    return (
      <div className="App">
        <header className="App-header">
          
          <p>
            Test fincollect app
          </p>

        </header>
        <div className="form-block">
          
          <label><b>Amount</b></label>
          <input type="text" name="amount" onChange={this.handleChange}/>
          
          <label><b>From</b></label>
          <select name="fromCurrency" onChange={this.handleChange}>
            {this.state.currencies.map((curr) => 
            <option value={curr.value} key={curr.value}>{curr.shortName}</option> 
            )}           
          </select>

          <label><b>To</b></label>
          <select name="toCurrency" onChange={this.handleChange}>
            {this.state.currencies.map((curr) => 
            <option value={curr.value} key={curr.value}>{curr.shortName}</option> 
            )}
          </select>         
          
          <button onClick={this.getRate}>Get rate</button>
        </div>
        <div>
          <p>Rate</p>
          <p>{ rate }</p>
          <p>Total Amount</p>
          <p>{ total }</p>
        </div>
      </div>
    );
  }
}

export default App;
