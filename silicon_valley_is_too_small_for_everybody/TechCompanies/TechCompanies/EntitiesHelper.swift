//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Nathan McCann on 5/30/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

class EntitiesHelper{
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    
    static func getSchools() -> [Entity]!{
        if listOfSchool == nil{
            listOfSchool.append(Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School))
        }
    return listOfSchool
    }
    static func getTechCompanies() -> [Entity]!{
        if listOfTechCompany == nil{
            listOfSchool.append(Entity(name: "Linkedin", town: "San Francisco", imageName: "linkedin", type: .TechCompany))
            listOfSchool.append(Entity(name: "Docker", town: "San Francisco", imageName: "docker", type: .TechCompany))
            listOfSchool.append(Entity(name: "Google", town: "Mountain View", imageName: "google", type: .TechCompany))
            listOfSchool.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
            listOfSchool.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
            listOfSchool.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
        }
    return listOfTechCompany
    }
}