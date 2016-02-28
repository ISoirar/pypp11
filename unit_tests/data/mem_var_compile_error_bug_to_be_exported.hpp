// Copyright 2004-2008 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#ifndef __mem_var_compile_error_bug_to_be_exported_hpp__
#define __mem_var_compile_error_bug_to_be_exported_hpp__

#include <map>

namespace sptCore
{

//! \brief Representation of connection between two 3d points
//! \author ShaXbee
class Path
{

public:
    //! Return reversed path
    Path* reverse() const { return NULL; }

    float length() const { return _length; }
    float frontRoll() const { return _frontRoll; }
    float backRoll() const { return _backRoll; }

    typedef std::pair<Path*, Path*> Pair;

private:
    float _length;
    float _frontRoll;
    float _backRoll;

}; // class sptCore::Path

//! \brief Abstract representation of Tracking in Scenery
//! \author Zbyszek "ShaXbee" Mandziejewicz
class RailTracking
{

public:
    virtual ~RailTracking() { };

    //! Get tracking exit for given entry point
    //! Throws UnknownEntryException if there is no exit for given entry
    virtual void getExit() const = 0;

    //! Get path that begins at given position
    //! Throws UnknownEntryException if there is no path for given entry
    virtual Path* getPath() const = 0;

}; // class sptCore::RailTracking

class Track: public RailTracking
{

public:
    virtual ~Track() { };

    virtual void getExit() const{}
    virtual Path* getPath() const{return NULL;}

    virtual Path* getDefaultPath() const { return NULL; };

private:
    // Py++: Removing this line makes wrapper compilable
    Path::Pair _path;

};

} // namespace sptCore

#endif//__mem_var_compile_error_bug_to_be_exported_hpp__
