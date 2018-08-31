//
//  ViewController.m
//  ChuckNorris
//
//  Created by Dimitri Merejkowsky on 31/08/2018.
//  Copyright © 2018 Dimitri Merejkowsky. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UITextView *textView;
@property (weak, nonatomic) IBOutlet UIButton *button;

@end

@implementation ViewController

- (IBAction)onClick:(id)sender {
  self.textView.text = @"hello";
}

- (void)viewDidLoad {
  [super viewDidLoad];
  // Do any additional setup after loading the view, typically from a nib.
}


- (void)didReceiveMemoryWarning {
  [super didReceiveMemoryWarning];
  // Dispose of any resources that can be recreated.
}


@end
