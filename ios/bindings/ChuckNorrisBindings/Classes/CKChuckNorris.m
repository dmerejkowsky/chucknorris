#import "CKChuckNorris.h"
#include "CKChuckNorris+Private.m"

@implementation CKChuckNorris

-(instancetype)init {
  self = [super init];
  return [self createCkPtr];
}

-(NSString *)getFact {
  return [self getFactImpl];

}

+ (NSString*)versionString {
  return [self versionStringImpl];
}

@end
