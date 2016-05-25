//
//  ViewController.swift
//  TapperDemo
//
//  Created by William McCann on 5/25/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var tapsRequired:Int? = 0
    var tapsDone:Int = 0
    
    @IBOutlet weak var imgTitle: UIImageView!
    @IBOutlet weak var btnPlay: UIButton!
    @IBOutlet weak var txtfldHowMany: UITextField!
    @IBOutlet weak var lblTaps: UILabel!
    @IBOutlet weak var btnCoin: UIButton!
    
    @IBAction func clickPlay(sender: AnyObject) {
        if self.txtfldHowMany != nil && self.txtfldHowMany.text != "" {
            self.tapsRequired = Int(self.txtfldHowMany.text!)
        }
        if self.lblTaps != nil {
            self.imgTitle.hidden = true
            self.btnPlay.hidden = true
            self.txtfldHowMany.hidden = true
            
            self.lblTaps.hidden = false
            self.btnCoin.hidden = false
        }
    }

    @IBAction func clickCoin(sender: AnyObject) {
        self.tapsDone += 1
        if self.tapsDone >= self.tapsRequired{
            self.resetGame()
        }
        
        self.updateTapsLabel()        
    }
    
   
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        self.tapsRequired = 0
        self.tapsDone = 0
        
        self.txtfldHowMany.text = ""
        self.lblTaps.text = String(tapsDone) + " taps done!"
        
        self.imgTitle.hidden = false
        self.btnPlay.hidden = false
        self.txtfldHowMany.hidden = false
        
        self.lblTaps.hidden = true
        self.btnCoin.hidden = true
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func updateTapsLabel(){
        self.lblTaps.text = String(self.tapsDone) + " Taps!"
    }
    
    func resetGame(){
        self.tapsRequired = 0
        self.tapsDone = 0
        
        self.txtfldHowMany.text = ""
        self.lblTaps.text = String(tapsDone) + " taps done!"
        
        self.imgTitle.hidden = false
        self.btnPlay.hidden = false
        self.txtfldHowMany.hidden = false
        
        self.lblTaps.hidden = true
        self.btnCoin.hidden = true
    }


}


