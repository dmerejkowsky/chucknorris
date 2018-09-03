//
//  ChuckNorrisBindingsTests.m
//  ChuckNorrisBindingsTests
//
//  Created by Dimitri Merejkowsky on 08/31/2018.
//  Copyright (c) 2018 Dimitri Merejkowsky. All rights reserved.
//

// https://github.com/Specta/Specta

#import "CKChuckNorris.h"

SpecBegin(ChuckNorris)

describe(@"ChuckNorris", ^{

    it(@"can get version", ^{
      expect([CKChuckNorris versionString]).to.equal(@"0.1");
    });
});

SpecEnd

