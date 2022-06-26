//
//  ContentView.swift
//  stocknotfier
//
//  Created by codingdudepy on 6/25/22.
//

import SwiftUI



struct ContentView: View {
    var body: some View {
        
        VStack{
            Text("Stock Notifier")
                .font(.headline)
                .position(x: 190, y: 50)

            Button("Get Started", action: executeDelete)
                .position(x: 190, y: 50)


    }
    }

    func executeDelete() {
        print("Now deleting…")
    }
   
    
        }
            



struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

